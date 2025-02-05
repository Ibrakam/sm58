from fastapi import FastAPI
from api.photos import photo_router
from db import Base, engine
# Для создания бд
Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
