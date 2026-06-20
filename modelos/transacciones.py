from pydantic import BaseModel


class TransaccionBase(BaseModel):
    cantidad: int
    valor_total: float
    factura_id: int
    
class TransaccionCrear(TransaccionBase):
    pass    

class TransaccionEditar(TransaccionBase):
    pass    

class Transaccion(TransaccionBase):
    id: int | None = None