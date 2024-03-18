
import mysql.connector as mysql
from dotenv import load_dotenv
import os
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

def connect(db_name):
    try:
        return mysql.connect(
        host="localhost",
        user="root",
        password=PASSWORD,
        database=db_name
        )
    except Exception as e:
        print("Error connecting to database", e)
        

if __name__ == "__main__":
    db = connect("projects")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    projet_records = cursor.fetchall()
    print(projet_records)
    db.close()