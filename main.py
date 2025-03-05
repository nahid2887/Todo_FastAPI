from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.database import engine, Base
from routes import web

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes
app.include_router(web.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}