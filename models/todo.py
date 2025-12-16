from sqlalchemy import Column, Integer, String,Boolean
from utils.database import Base 


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    task_name  = Column(String)
    is_completed = Column(Boolean, default=False)
    pass 