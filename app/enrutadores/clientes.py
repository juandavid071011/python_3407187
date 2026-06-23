from fastapi import APIRouter, HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar

rutas_clientes = APIRouter()
lista_clientes: list[Cliente] = []

# listar todos los clientes de la lista 
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return {lista_clientes}


# listar un solo cliente de la lista 
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")


# crear un cliente en la lista
@rutas_clientes.post("/clientes", response_model=Cliente)  # respuest todos los datos del cliente
async def crear_clientes(datos_cliente: ClienteCrear):  # creacion sin el id.
    # validar datos_cliente, pasar json a dicccionario
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

# editar un cliente en la lista
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for  i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            # validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes [i] = cliente_val
            return cliente_val
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")

    
# eliminar un cliente de la lista
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_clientes(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")