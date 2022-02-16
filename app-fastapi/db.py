from psycopg2 import pool
from psycopg2.extras import RealDictCursor
# No print statements to avoid io operations

connection_pool = pool.SimpleConnectionPool(1,
                                            5,
                                            host="localhost",
                                            port=5432,
                                            database="test",
                                            user="postgres",
                                            password="fr24Password")


"""
Queries 
"SELECT * from counties limit 10;"

"SELECT * from counties WHERE id = {id}
"""

def get_top_10():
    conn = connection_pool.getconn()
    values = None
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute("SELECT * from counties limit 10;")
        values = cursor.fetchall()
    connection_pool.putconn(conn)
    return values

def get_one_country(id_):
    conn = connection_pool.getconn()
    values = None
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        values = cursor.execute(f"SELECT * from counties WHERE id = {id_}")
        values = cursor.fetchall()
    connection_pool.putconn(conn)
    return values