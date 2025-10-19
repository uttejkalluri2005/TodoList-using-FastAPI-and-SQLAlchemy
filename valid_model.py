from pydantic import BaseModel

class todoAdd(BaseModel):
    taskid:int
    taskname:str
    Priority:str 

class todoUpdate(BaseModel):
    taskname:str
    Priority:str

