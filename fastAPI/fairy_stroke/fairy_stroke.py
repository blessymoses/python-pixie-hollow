from fastapi import FastAPI
from pydantic import BaseSettings
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# pydantic settings
class Settings(BaseSettings):
    message: str = "Default msg"


settings = Settings()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home():
    return {"Howdy": "Fairy"}


@app.get("/settings")
def get_settings():
    return {"message": settings.message}


@app.post("/")
async def home():
    return {"Howdy": "Post!"}


# URL parameters - /employee/10
@app.get("/employee/{id}")
def home(id: int):
    return {"id": id}


# query parameters - /employee?department=cse
@app.get("/employee")
def home(department: str):
    return {"department": department}


@app.get("/quote/{name}", response_class=HTMLResponse)
async def get_name(request: Request, name: str):
    return templates.TemplateResponse(
        ("index.html", {"request": request, "name": name})
    )
