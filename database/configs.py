from config_schemes import (
    DataBaseConfig,
    ConnectionAlias,
    MySQLCredentials,
    MySQLConnectionConfig,
)

MYSQL_CONFIG = DataBaseConfig(
    connections={
        ConnectionAlias.MYSQL: MySQLConnectionConfig(
            engine='tortoise.backends.mysql',
            credentials=MySQLCredentials(
                host='localhost',
                port=3307,
                user='root',
                password='root',
                database='dev'
            )
        ),
    },
    apps={},
)
