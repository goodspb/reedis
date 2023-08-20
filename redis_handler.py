import redis
from redis.sentinel import Sentinel
from redis.cluster import RedisCluster
from sshtunnel import SSHTunnelForwarder

from database import Connection


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
            decode_responses=True,
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
            decode_responses=True,
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


def get_keys(r, match_text = None):
    keys = r.scan_iter(match=match_text)
    key_list = []
    for key in keys:
        key_list.append(key)
    return key_list
