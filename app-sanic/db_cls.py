from psycopg2 import pool
# Could be improved but it is fine for now and it is not being used

class Database:
    connection_pool = None

    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(1,
                                                    5,
                                                    host="localhost",
                                                    port=5432,
                                                    database="test",
                                                    user="postgres",
                                                    password="fr24Password")
    
    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.connection_pool.putconn(connection) 
    
    @classmethod
    def close_all_connections(cls):
        cls.connection_pool.closeall()


class CursorFromConnPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor().close()
            self.connection.commit()
            Database.return_connection(self.connection)
    
