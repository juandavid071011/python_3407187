from pydantic import BaseModel, computed_field
from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime

class FacturasBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente
    transaccones: list[Transaccion] = []
    
    @computed_field
    @property
    def vr_total (self) -> float:
        return vr_total
class FacturaCrear(FacturasBase):
    pass

class FacturaEditar(FacturasBase):
    pass

class Factura(FacturasBase):
    id: int | None = None