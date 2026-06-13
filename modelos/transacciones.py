from pydantic import BaseModel


class transsacciones(BaseModel):
    id: int
    cantidad: int
    vr_total: float
    factura_id: int