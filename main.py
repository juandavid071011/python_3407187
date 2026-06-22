from fastapi import FastAPI, HTTPException, status
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# listar todos los clientes de la lista 
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return {"clientes": lista_clientes}


# listar un solo cliente de la lista 
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")


# crear un cliente en la lista
@app.post("/clientes", response_model=Cliente)  # respuest todos los datos del cliente
async def crear_clientes(datos_cliente: ClienteCrear):  # creacion sin el id.
    # validar datos_cliente, pasar json a dicccionario
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

# editar un cliente en la lista
@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for  i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes [i] = cliente_val
            return cliente_val
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")

    
# eliminar un cliente de la lista
@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_clientes(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
        raise HTTPException(status_code=400, detail=f"El Cliente con id {cliente_id} no existe")

# listar todas las facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

#listar una sola factura
@app.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
   for i, obj_factura in enumerate(lista_facturas):
           if obj_factura.id == id_factura:
               return obj_factura
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {id_factura} no existe")


#  crear facturas
@app.post("/facturas{id_cliente}", response_model=Factura)
async def crear_facturas(id_cliente: int, datos_factura: FacturaCrear):
    #buscar cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
       if cliente.id == id_cliente:
           cliente_encontrado = cliente
    # si no existe cliente 
    if not cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {id_cliente} no existe") 


    # validar datos factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    # id de la factura
    factura_val.id = len(lista_facturas)
    lista_facturas.append(factura_val)
    return factura_val

# de editar facturas
@app.put("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

# endpoint de eliminar facturas
@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass

# endpoints de transacciones
# listar todas las transacciones
@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# listar una sola transaccion
@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def obtener_transaccion(id_transaccion: int):
    pass

# crear transacciones
@app.post("/transacciones/{id_factura}", response_model=Transaccion)
async def crear_transaccion(id_factura: int, datos_transaccion: TransaccionCrear):
    #buscar factura
        factura_encontrada = None
        for factura in lista_facturas:
           if factura.id == id_factura:
               factura_encontrada = factura
        # si no existe factura 
        if not factura_encontrada:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {id_factura} no existe") 
    
        # validar datos de la transaccion
        transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
        transaccion_val.factura_id = id_factura
        factura_encontrada.transaccones.append(transaccion_val)
        # id de la factura
        transaccion_val.id = len(lista_transacciones) + 1
        return transaccion_val
        

# editar transacciones
@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass

# endpoint de eliminar transacciones
@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass