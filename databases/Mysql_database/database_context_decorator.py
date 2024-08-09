from contextlib import contextmanager

import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
HOST=os.getenv('DATABASE_URL')
USER=os.getenv('DATABASE_USER')
SCHEMA=os.getenv('SCHEMA')

@contextmanager
def database(host, username, password, database):
        conn = mysql.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        
        yield cursor
        conn.close()
        

def read_data(table_name):
    with database(HOST, USER, PASSWORD, SCHEMA) as cursor:
        query = "SELECT * FROM {}".format(table_name)
        cursor.execute(query)
        projet_records = cursor.fetchall()
        print(projet_records)
        

def read_projects():
    read_data("projects")
    
def read_task():
    read_data("tasks")
    
if __name__ == "__main__":
    read_projects()
    read_task()