from pydantic import BaseModel
from .clientes import Cliente


class FacturasBase(BaseModel):
    fecha: str
    valor_total: float
    cliente: Cliente
    
class FacturaCrear(FacturasBase):
    pass

class FacturaEditar(FacturasBase):
    pass

class Factura(FacturasBase):
    id: int | None = None