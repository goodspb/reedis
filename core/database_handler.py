from typing import Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from util.setting_util import get_user_setting_dir

db_file = get_user_setting_dir() + "reedis.db"
print(f"db_file: {db_file}")

engine = create_engine(f'sqlite:///{db_file}?check_same_thread=False', echo=True)

Base = declarative_base()


class Connection(Base):
    __tablename__ = 'connections'
    id = Column(Integer, primary_key=True, autoincrement="auto", index=True)
    host = Column(String(255), )
    port = Column(Integer, default=6379)
    username = Column(String(255), default="")
    password = Column(String(255), default="")
    ssh = Column(Boolean, default=False)
    ssl = Column(Boolean, default=False)
    sentinel = Column(Boolean, default=False)
    cluster = Column(Boolean, default=False)
    readonly = Column(Boolean, default=False)
    ssh_host = Column(String(255), default="")
    ssh_port = Column(String(255), default="")
    ssh_username = Column(String(255), default="")
    ssh_password = Column(String(255), default="")
    ssh_private_key = Column(String(255), default="")
    ssh_passphrase = Column(String(255), default="")
    ssh_timeout = Column(Integer, default=30)
    ssl_public_key = Column(String(255), default="")
    ssl_private_key = Column(String(255), default="")
    ssl_authority = Column(String(255), default="")
    sentinel_master_group_name = Column(String(255), default="")
    sentinel_redis_node_password = Column(String(255), default="")


Base.metadata.create_all(engine, checkfirst=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

session = SessionLocal()


def get_db_session():
    return session


def get_connections() -> list[Type[Connection]]:
    return get_db_session().query(Connection).all()


def get_connection(cid) -> Optional[Connection]:
    if not cid:
        return None
    return get_db_session().query(Connection).filter_by(id=cid).first()


def add_or_edit_connections(connection: Connection, create=False) -> (bool, str):
    s = get_db_session()
    # add
    if create:
        s.add(connection)
    # update
    s.commit()
    return True, ''


def delete_connection(cid):
    s = get_db_session()
    connection = get_connection(cid)
    if not connection:
        return False
    s.delete(connection)
    s.commit()
    return True
