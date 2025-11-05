from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer,Column,String,create_engine,DATE,MetaData
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv("pass.env")

db_url = os.getenv("db_url")
engine = create_engine(db_url)
session = sessionmaker(autoflush=False,bind=engine)
Base = declarative_base()

class todo(Base):
    __tablename__ = "todolist"
    taskid = Column(Integer,primary_key=True)
    taskname = Column(String)
    Priority = Column(String)

Base.metadata.create_all(engine)
