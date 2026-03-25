from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar(self, total: float) -> float:
        pass

class DescuentoNavideno(EstrategiaDescuento):
    def aplicar(self, total: float): return total * 0.90 # 10% off

class SinDescuento(EstrategiaDescuento):
    def aplicar(self, total: float): return total

class Carrito:
    def __init__(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia
    
    def calcular_total(self, monto: float):
        return self.estrategia.aplicar(monto)