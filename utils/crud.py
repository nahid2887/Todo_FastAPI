from sqlalchemy.orm import Session
from models.todo import Todo


def get_todos(db: Session,skip:int=0, limit:int=100):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: dict):
    db_todo = Todo(**todo)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo_id: int, todo_data: dict):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
    return db_todo