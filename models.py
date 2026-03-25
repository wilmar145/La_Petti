from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

# --- Clase existente de Usuarios ---
class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    correo = Column(String(100), unique=True)
    # Puedes tener más campos aquí...

# --- AQUÍ PEGA LA NUEVA CLASE PRODUCTO ---
class Producto(Base):
    __tablename__ = "producto"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    precio = Column(Float)  # Verifica que sea Float o Decimal
    stock = Column(Integer)

# --- Clase para el Patrón State (Opcional si ya la tienes) ---
class Pedido(Base):
    __tablename__ = "pedido"
    id_pedido = Column(Integer, primary_key=True, index=True)
    estado = Column(String(50), default="Emitido") # Para el Punto 1
    total = Column(Float)