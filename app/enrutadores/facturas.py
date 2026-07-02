from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer, facturaLeerCompuesta
from ..modelos.clientes import Cliente, ClienteLeer
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import Sesion_independecia
from sqlmodel import select

rutas_facturas = APIRouter()

#lista_clientes: list[Cliente] = []
#lista_facturas: list[Factura] = []


# listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Sesion_independecia):
    consulta =select(Factura)
    lista_facturas =sesion.exec(consulta).all()
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
async def crear_facturas(id_cliente: int, datos_factura: FacturaCrear, sesion: Sesion_independecia):
    #buscar cliente
    cliente_encontrado = sesion.get(Cliente, id_cliente)
    # si no existe cliente 
    if not cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {id_cliente} no existe") 


    # validar datos factura
    factura_dict = datos_factura.model_dump()
    factura_dict["id_cliente"] = id_cliente
    factura_val = Factura.model_validate(factura_dict)
    #guardar en base de datos
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val

# de editar facturas
@rutas_facturas.put("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

# endpoint de eliminar facturas
@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    pass