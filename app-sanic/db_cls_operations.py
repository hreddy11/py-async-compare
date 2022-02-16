from db_cls import Database, CursorFromConnPool
from psycopg2.extras import RealDictCursor
import json
# could be improved but it is not being used

"""
Queries 
"SELECT * from counties limit 10;"

"SELECT * from counties WHERE id = {id}
"""
Database.initialise()

def get_top_10():
    values = None

    with CursorFromConnPool() as cursor:
        cursor = cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * from counties limit 10;")
        values = cursor.fetchall()

    if values != None:
        values = json.dumps(values)

    return values

def get_one_country(id_):
    values = None

    with CursorFromConnPool() as cursor:
        cursor = cursor(cursor_factory=RealDictCursor)
        values = cursor.execute(f"SELECT * from counties WHERE id = {id_}")
        values = cursor.fetchall()

    if values != None:
        values = json.dumps(values)
    return values