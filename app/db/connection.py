
class DbConnection:
    user = 'root'
    password = 'root'
    host = 'mariadb'
    port = 3306
    default_db = 'common'
    driver = 'mysql+mysqlconnector'

    conn_string_pattern = '{}://{}:{}@{}:{}/{}'

    @staticmethod
    def get_conn_string(db=default_db):
        return DbConnection.conn_string_pattern.format(
            DbConnection.driver,
            DbConnection.user,
            DbConnection.password,
            DbConnection.host,
            DbConnection.port,
            db
        )
