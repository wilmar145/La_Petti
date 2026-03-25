from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Producto

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/")
def crear_producto(nombre: str, precio: float, stock: int, db: Session = Depends(get_db)):
    nuevo = Producto(nombre=nombre, precio=precio, stock=stock)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/")
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()