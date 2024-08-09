import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
HOST=os.getenv('DATABASE_URL')
USER=os.getenv('DATABASE_USER')
SCHEMA=os.getenv('SCHEMA')

class Database:
    def __init__(self, host, username, password, database):
        self.host = host
        self.user = username
        self.password = password
        self.database = database
        
    def __enter__(self):
        self.conn = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, trace):
        self.conn.close()
        

def read_data(table_name):
    with Database(HOST, USER, PASSWORD, SCHEMA) as cursor:
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