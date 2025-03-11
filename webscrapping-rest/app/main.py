from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scraper API", version="1.0")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Scraper API is running!"}
