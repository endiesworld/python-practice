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
        self.conn.commit()
        self.conn.close()
        

def read_data(table_name):
    with Database(HOST, USER, PASSWORD, SCHEMA) as cursor:
        query = "SELECT * FROM {}".format(table_name)
        cursor.execute(query)
        projet_records = cursor.fetchall()
        print(projet_records)
        
        
def add_project(project_datas=[]):
    last_row_id = None
    with Database(HOST, USER, PASSWORD, SCHEMA) as cursor:
        for project_data in project_datas:
            query = """ INSERT INTO projects(title, description) VALUES (%s, %s) """
            cursor.execute(query, project_data)
        last_row_id = cursor.lastrowid
    return last_row_id

def add_tasks(project_id, tasks=[]):
    tasks_data = []
    with Database(HOST, USER, PASSWORD, SCHEMA) as cursor:
        for task in tasks:
            task_data = (project_id, task)
            tasks_data.append(task_data)
        query = """ INSERT INTO tasks(project_id, description) VALUES (%s, %s) """
        cursor.executemany(query, tasks_data)


def read_projects():
    read_data("projects")
    
def read_task():
    read_data("tasks")
    

    
if __name__ == "__main__":
    TASK = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    projects = [("Clean house", "Clean house by room")]
    # read_projects()
    # read_task()
    project_id = add_project(projects)
    add_tasks(project_id, TASK)