from pydantic import BaseModel
from .clientes import Cliente


class Facturas(BaseModel):
    id: int
    fecha: str
    valor_toital: float
    cliente: Cliente