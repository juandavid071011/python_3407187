from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime

class FacturasBase(SQLModel):
    fecha: str = Field(default=datetime.now)
    # cliente: Cliente
    # transaccones: list[Transaccion] = []
    
    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        if  self.transaccones == None:
            return total_factura
    #recorrer la lista de transacciones, segun el id de la factura actual
        for transaccion in self.transaccones:
            total_factura += transaccion.vr_unitario * transaccion.cantidad
        return total_factura
        
        
        
class FacturaCrear(FacturasBase):
    pass

class FacturaEditar(FacturasBase):
    pass

class Factura(FacturasBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id") 
    #crear relaciones virtuales con cliente, transacciones . no en la bd
    cliente: Cliente = Relationship(back_populates="factura") 
    trasacciones: list[Transaccion] = Relationship(back_populates="factura")
    

# crea modelo para mostrar la usuario o el cliente
class FacturaLeer(FacturasBase):
    id: int
    cliente: ClienteLeer
    #pero no es reconmedable, por las buenas practicas 
    #transacciones: list[TransaccionLeer] = []
class FacturaLeerCompuesta(FacturaLeer):
    trasacciones: list[Transaccion] = []