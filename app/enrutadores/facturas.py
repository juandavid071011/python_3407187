from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas

rutas_facturas = APIRouter()

#lista_clientes: list[Cliente] = []
#lista_facturas: list[Factura] = []


# listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

#listar una sola factura
@rutas_facturas.get("/facturas/{id_factura}", response_model=Factura)
async def listar_factura(id_factura: int):
   for i, obj_factura in enumerate(lista_facturas):
           if obj_factura.id == id_factura:
               return obj_factura
           raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {id_factura} no existe")


#  crear facturas
@rutas_facturas.post("/facturas/{id_cliente}", response_model=Factura)
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
@rutas_facturas.put("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

# endpoint de eliminar facturas
@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    pass