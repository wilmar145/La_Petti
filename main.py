from fastapi import FastAPI
from app.database import engine, Base
import app.models.models as models
from app.routers import usuarios, productos # Asegúrate de que no haya texto extra aquí
app = FastAPI(title="Le Petit Café API")

# Esto crea las tablas en MySQL
models.Base.metadata.create_all(bind=engine)

# Registrar el router del CRUD de Usuarios
app.include_router(usuarios.router) 
app.include_router(productos.router)
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a Le Petit Café"}