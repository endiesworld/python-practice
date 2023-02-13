from typing import Optional
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    active = "active"

@app.get('/ping')
def my_function(name: Optional[ModelName] = None):
    return {"msg": f'Hello world! {name}'}
    
    
    

