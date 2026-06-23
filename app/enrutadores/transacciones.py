from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_facturas, lista_transacciones

rutas_transacciones = APIRouter()

#lista_facturas: list[Factura] = [] 
#lista_transacciones: list[Transaccion] = []

# endpoints de transacciones
# listar todas las transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# listar una sola transaccion
@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def obtener_transaccion(id_transaccion: int):
    pass

# crear transacciones
@rutas_transacciones.post("/transacciones/{id_factura}", response_model=Transaccion)
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
        lista_transacciones.append(transaccion_val)
        return transaccion_val
        

# editar transacciones
@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass

# endpoint de eliminar transacciones
@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass