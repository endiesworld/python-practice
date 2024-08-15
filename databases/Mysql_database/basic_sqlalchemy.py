from dotenv import load_dotenv
import os

import sqlalchemy

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
HOST=os.getenv('DATABASE_URL')
USER=os.getenv('DATABASE_USER')
SCHEMA=os.getenv('SCHEMA')
PORT=os.getenv('PORT')

db_engine = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}"
engine = sqlalchemy.create_engine(db_engine, echo=True)
