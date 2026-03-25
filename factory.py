from app.models.models import Cliente, Empleado

class UsuarioFactory:
    @staticmethod
    def get_usuario(tipo_usuario: str, datos: dict):
        if tipo_usuario == "cliente":
            return Cliente(**datos)
        elif tipo_usuario == "empleado":
            return Empleado(**datos)
        else:
            raise ValueError("Tipo de usuario no soportado")