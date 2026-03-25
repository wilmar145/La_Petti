from pydantic import BaseModel, EmailStr
from typing import Optional, List
from decimal import Decimal

# --- Esquemas para el Módulo de Usuarios (Cliente) ---
class ClienteBase(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    password: str

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class ClienteResponse(ClienteBase):
    id_cliente: int
    class Config:
        from_attributes = True

# --- Esquemas para el Módulo de Productos (Tu elemento adicional) ---
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: Decimal
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id_producto: int
    class Config:
        from_attributes = True