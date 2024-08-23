from dotenv import load_dotenv
import os

from sqlalchemy import Column, String, Integer, ForeignKey, select, create_engine
from sqlalchemy.orm import registry, relationship, Session

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
HOST=os.getenv('DATABASE_URL')
USER=os.getenv('DATABASE_USER')
SCHEMA=os.getenv('SCHEMA')
PORT=os.getenv('PORT')

db_engine = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}"
engine = create_engine(db_engine, echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))
    
    def __repr__(self):
        return "<Project(title='{0}, description='{1}')>".format(self.title, self.description)
    
    
class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))
    
    project = relationship("Project")
    
    def __repr__(self):
        return "<description='{0}')>".format(self.description)
    
Base.metadata.create_all(engine)

with Session(engine) as session:
    smt = select(Project).where(Project.title == 'Organize closet')
    results = session.execute(smt)
    # Scalar allows us to retrieve the first row returned in the results.
    organize_closet_project = results.scalar()
    
    smt = select(Task).where(Task.project_id == organize_closet_project.project_id)
    results = session.execute(smt)
    for task in results:
        print(task)