from fastapi import FastAPI,Depends,Form,Path
import uvicorn
from sqlalchemy.orm import Session
from database import session,todo
from valid_model import todoAdd,todoUpdate
app=FastAPI()

def get_data():
    db: Session = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/root")
def get_table(db: Session = Depends(get_data)):
    product = db.query(todo).all()
    return product

@app.post("/add")
def get_task(task_data:todoAdd, db: Session = Depends(get_data)):
    new_task = todo(taskid=task_data.taskid,
                    taskname=task_data.taskname,
                    Priority=task_data.Priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    if new_task:
        return {"Message":"New data Added.","task":new_task}
    else:
        return {"Message":"No new data found or has been invalidated"}

@app.put("/update/{taskid}")
def update_data(task_data : todoUpdate, taskid:int =Path(...), db:Session = Depends(get_data)):
      updates = db.query(todo).filter(todo.taskid==taskid).first()
      updates.taskname = task_data.taskname
      updates.Priority = task_data.Priority
      db.commit()

@app.delete("/del/{taskid}")
def del_data(taskid:int = Path(),db: Session = Depends(get_data)):
    task = db.query(todo).filter(todo.taskid==taskid).first()
    db.delete(task)
    db.commit()






