import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
HOST=os.getenv('DATABASE_URL')
USER=os.getenv('DATABASE_USER')
SCHEMA=os.getenv('SCHEMA')

def connect():
    try:
        return mysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=SCHEMA
        )
    except Exception as e:
        print("Error connecting to database", e)
        

if __name__ == "__main__":
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    projet_records = cursor.fetchall()
    print(projet_records)
    db.close()