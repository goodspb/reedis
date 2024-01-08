import redis
import sshtunnel
from redis.sentinel import Sentinel
from redis.cluster import RedisCluster

from core.database_handler import Connection


def get_redis_connection(connection: Connection):
    redis_host = connection.host
    redis_port = connection.port
    if connection.ssh:
        try:
            server = sshtunnel.SSHTunnelForwarder(
                (connection.ssh_host, int(connection.ssh_port)),
                ssh_username=connection.ssh_username,
                ssh_password=connection.ssh_password,
                ssh_pkey=connection.ssh_private_key if connection.ssh_private_key else None,
                ssh_private_key_password=connection.ssh_passphrase if connection.ssh_passphrase else None,
                remote_bind_address=(connection.host, int(connection.port)),
            )
            server.start()
            print(f"get_redis_connection sshtunnel: {server}")
            redis_host = server.local_bind_host
            redis_port = server.local_bind_port
        except sshtunnel.BaseSSHTunnelForwarderError as e:
            print(f"get_redis_connection sshtunnel error: {e}")
            return False, None
    if connection.sentinel:
        sentinel = Sentinel([(redis_host, redis_port)])
        r = sentinel.master_for(connection.sentinel_master_group_name, password=connection.sentinel_redis_node_password)
    elif connection.cluster:
        r = RedisCluster(
            host=redis_host,
            port=redis_port,
            db=0,
            password=connection.password if connection.password else None,
            ssl=connection.ssl,
            ssl_keyfile=connection.ssl_private_key if connection.ssl_private_key else None,
            ssl_certfile=connection.ssl_public_key if connection.ssl_public_key else None,
            ssl_ca_path=connection.ssl_authority if connection.ssl_authority else None,
        )
    else:
        r = redis.Redis(
            host=redis_host,
            port=redis_port,
            db=0,
            password=connection.password if connection.password else None,
            ssl=connection.ssl,
            ssl_keyfile=connection.ssl_private_key if connection.ssl_private_key else None,
            ssl_certfile=connection.ssl_public_key if connection.ssl_public_key else None,
            ssl_ca_path=connection.ssl_authority if connection.ssl_authority else None,
        )
    try:
        r.ping()
        return True, r
    except redis.ConnectionError as e:
        print(f"get_redis_connection ConnectionError: {redis_host}:{redis_port}")
        print(f"get_redis_connection ConnectionError: {e}")
        return False, None
    except redis.RedisError:
        print(f"get_redis_connection RedisError: {redis_host}:{redis_port}")
        return False, None


def get_dbs(r):
    db_count = r.config_get('databases')['databases']
    return int(db_count)


def get_keys(r, cursor=0, match_text="*", count=100):
    match_text = "*" if not match_text else match_text
    new_cursor, keys = r.scan(cursor=cursor, match=match_text, count=count)
    print(f"get_keys: {new_cursor}, keys:{keys}")
    return new_cursor, [key.decode('utf-8', errors='ignore') for key in keys]
