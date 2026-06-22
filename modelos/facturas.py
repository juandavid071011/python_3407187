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
        # calcular (cantidad * vr_total)
        # consular el id actual de factura
        factura_id_actual = getattr(self, 'id', None)
        total_factura = 0.0
        if not factura_id_actual or not self.transaccones:
            return total_factura
        #recorrer la lista de transacciones, segun el id de la factura actual
        for transaccion in self.transaccones:
            if transaccion.factura.id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad
        return total_factura
        
        
        
class FacturaCrear(FacturasBase):
    pass

class FacturaEditar(FacturasBase):
    pass

class Factura(FacturasBase):
    id: int | None = None