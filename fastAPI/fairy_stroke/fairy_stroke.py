from fastapi import FastAPI
from pydantic import BaseSettings

# pydantic settings
class Settings(BaseSettings):
    message: str = "Default msg"


settings = Settings()
app = FastAPI()


@app.get("/")
async def home():
    return {"Howdy": "Fairy"}


@app.get("/settings")
def get_settings():
    return {"message": settings.message}
