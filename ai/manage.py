from fastapi import FastAPI
from api.routes import router
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
app.include_router(router)

os.makedirs("static/generated", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
