import sqlite3
from contextlib import contextmanager


@contextmanager
def database_connection(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    yield cursor
    
    conn.commit()
    conn.close()
    

with database_connection("mydb.db") as c:
    c.execute("CREATE TABLE IF NOT EXISTS person (name VARCHAR(255) NOT NULL, age INT);")