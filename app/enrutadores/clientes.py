from fastapi import APIRouter, HTTPException, status
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes
from ..conexion_bd import Sesion_independecia
from sqlmodel import select

rutas_clientes = APIRouter()
#lista_clientes: list[Cliente] = []

# listar todos los clientes de la lista 
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: Sesion_independecia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli


# listar un solo cliente de la lista 
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)

async def listar_cliente(cliente_id: int, mi_sesion: Sesion_independecia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El Cliente con id {cliente_id} no existe")
    
    return cliente_bd

# crear un cliente en la lista
@rutas_clientes.post("/clientes", response_model=Cliente)  # respuest todos los datos del cliente
async def crear_clientes(datos_cliente: ClienteCrear, mi_sesion: Sesion_independecia): # creacion sin el id.
    # validar datos_cliente, pasar json a dicccionario
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val

# editar un cliente en la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar, mi_sesion: Sesion_independecia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El Cliente con id {cliente_id} no existe")
        
    cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dict)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_bd)
    return cliente_bd
# eliminar un cliente de la lista
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_clientes(cliente_id: int, mi_sesion: Sesion_independecia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El Cliente con id {cliente_id} no existe")
    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()
    return cliente_bd        