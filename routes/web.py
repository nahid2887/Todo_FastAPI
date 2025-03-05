from fastapi import APIRouter, Request, HTTPException, Depends, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from utils.crud import get_todo, delete_todo, update_todo, create_todo, get_todos
from database.database import get_db
from schemas.todo import TodoCreat
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def list_todos(request: Request, db: Session = Depends(get_db)):
    todos = get_todos(db)
    return templates.TemplateResponse("/todos/list.html", {"request":request, "todos":todos})

@router.get("/create", response_class=HTMLResponse)
async def create_todo_form(request: Request):
    return templates.TemplateResponse("todos/form.html", {"request":request, "todo":None})

@router.post("/create", response_class=HTMLResponse)
async def create_todo_submit(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    completed : bool= Form (False),
    db: Session = Depends(get_db)
):
    todo_data = {"title": title, "description": description, "completed": completed}
    create_todo(db, todo_data)
    return RedirectResponse(url="/", status_code=303)

@router.get("/{todo_id}", response_class=HTMLResponse)
async def view_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return templates.TemplateResponse("todos/detail.html", {"request": request, "todo": todo})

@router.get("/{todo_id}/edit", response_class=HTMLResponse)
async def edit_todo_form(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return templates.TemplateResponse("todos/form.html", {"request": request, "todo": todo})

@router.post("/{todo_id}/edit", response_class=HTMLResponse)
async def update_todo_submit(
    request: Request,
    todo_id: int,
    title: str = Form(...),
    description: str = Form(None),
    completed: bool = Form(False),
    db: Session = Depends(get_db)
):
    todo_data = {"title": title, "description": description, "completed": completed}
    update_todo(db, todo_id, todo_data)
    return RedirectResponse(url="/", status_code=303)

@router.get("/{todo_id}/delete", response_class=HTMLResponse)
async def delete_todo_submit(request: Request, todo_id: int, db: Session = Depends(get_db)):
    delete_todo(db, todo_id)
    return RedirectResponse(url="/", status_code=303)



