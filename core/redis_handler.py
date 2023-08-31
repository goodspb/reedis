import redis
from redis.sentinel import Sentinel
from redis.cluster import RedisCluster
from sshtunnel import SSHTunnelForwarder

from core.database_handler import Connection


def get_redis_connection(connection: Connection):
    if connection.ssh:
        server = SSHTunnelForwarder(
            ssh_username=connection.ssh_username,
            ssh_password=connection.ssh_password,
            ssh_address_or_host=(connection.ssh_host, connection.ssh_password),
            local_bind_address=('localhost', connection.port),
            remote_bind_address=(connection.host, connection.port),
            ssh_pkey=connection.ssh_private_key if connection.ssh_private_key else None,
            ssh_private_key_password=connection.ssh_passphrase if connection.ssh_passphrase else None,
        )
        server.daemon_forward_servers = True
        server.start()
        connection.host = 'localhost'
    if connection.sentinel:
        sentinel = Sentinel([(connection.host, connection.port)])
        r = sentinel.master_for(connection.sentinel_master_group_name, password=connection.sentinel_redis_node_password)
    elif connection.cluster:
        r = RedisCluster(
            host=connection.host,
            port=connection.port,
            db=0,
            password=connection.password if connection.password else None,
            ssl=connection.ssl,
            ssl_keyfile=connection.ssl_private_key if connection.ssl_private_key else None,
            ssl_certfile=connection.ssl_public_key if connection.ssl_public_key else None,
            ssl_ca_path=connection.ssl_authority if connection.ssl_authority else None,
        )
    else:
        r = redis.Redis(
            host=connection.host,
            port=connection.port,
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
    except redis.ConnectionError:
        return False, None


def get_dbs(r):
    db_count = r.config_get('databases')['databases']
    return int(db_count)


def get_keys(r, cursor=0, match_text="*", count=100):
    match_text = "*" if not match_text else match_text
    new_cursor, keys = r.scan(cursor=cursor, match=match_text, count=count)
    print(f"get_keys: {new_cursor}, keys:{keys}")
    return new_cursor, [key.decode('utf-8', errors='ignore') for key in keys]
