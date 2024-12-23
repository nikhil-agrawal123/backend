from fastapi import FastAPI
from . import models
from .database import engine
from .routers import main


app = FastAPI()
app.include_router(main.router)

models.Base.metadata.create_all(engine)