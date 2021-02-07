from enum import Enum
from typing import List, Dict

from pydantic import BaseModel


class MySQLCredentials(BaseModel):
    # host
    host: str = 'localhost'
    port: int = 3306
    # auth
    user: str = 'root'
    password: str = 'root'
    # db
    database: str


class MySQLConnectionConfig(BaseModel):
    engine: str = 'tortoise.backends.mysql'
    credentials: MySQLCredentials


class ConnectionAlias(str, Enum):
    MYSQL = 'mysql'

class AppConfig(BaseModel):
    models: List[str]
    default_connection: ConnectionAlias


class AppAlias(str, Enum):
    MOVIE = 'movie'


class DataBaseConfig(BaseModel):
    connections: Dict[ConnectionAlias, MySQLConnectionConfig]
    apps: Dict[AppAlias, AppConfig]

