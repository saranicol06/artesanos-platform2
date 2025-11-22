from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Artesano(BaseModel):
    nombre: str
    ubicacion: str
    tipo: str

@app.get("/")
def read_root():
    return {"message": "API Artesanos funcionando"}

@app.post("/api/artesanos", status_code=201)
def create_artesano(a: Artesano):
    return {"id": 1, **a.model_dump()}
