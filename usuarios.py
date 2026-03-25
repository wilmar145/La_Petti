from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Cliente # Usaremos la tabla Cliente para el CRUD

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# 1. CREAR (Create)
@router.post("/")
def crear_usuario(nombre: str, correo: str, db: Session = Depends(get_db)):
    nuevo = Cliente(nombre=nombre, correo=correo)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Usuario creado", "usuario": nuevo}

# 2. LEER (Read)
@router.get("/{id}")
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Cliente).filter(Cliente.id_cliente == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No existe")
    return usuario

# 3. ACTUALIZAR (Update)
@router.put("/{id}")
def actualizar_usuario(id: int, nuevo_nombre: str, db: Session = Depends(get_db)):
    usuario = db.query(Cliente).filter(Cliente.id_cliente == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No existe")
    usuario.nombre = nuevo_nombre
    db.commit()
    return {"mensaje": "Usuario actualizado"}

# 4. ELIMINAR (Delete)
@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Cliente).filter(Cliente.id_cliente == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No existe")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado"}