from pydantic import BaseModel


# modelo de clientes
class ClienteBase(BaseModel):
    # validacion con pydantic
    nombre: str
    email: str
    descripcion: str | None = None


class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int | None = None