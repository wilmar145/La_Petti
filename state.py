from abc import ABC, abstractmethod

class EstadoPedido(ABC):
    @abstractmethod
    def siguiente(self, pedido):
        pass

class EstadoEmitido(EstadoPedido):
    def siguiente(self, pedido):
        pedido.estado = "Enviado"

class EstadoEnviado(EstadoPedido):
    def siguiente(self, pedido):
        pedido.estado = "Entregado"