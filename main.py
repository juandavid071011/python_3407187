from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente
from modelos.facturas import Factura
 
app = FastAPI()

lista_clientes = []
lista_facturas = []


@app.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}

@app.post("/clientes", response_model=Cliente) #respuesta todos los datos del cliente creado.
def crear_cliente(datos_cliente: Clientecrear): #creacion sin el id.
    # genere un id segun lista_clientes
    id_cliente = len(lista_clientes)+1
    print(id_cliente)
    lista_clientes.append(datos_cliente)
    # return {"mensaje": "Cliente creado", "cliente": datos_cliente}
    return datos_cliente
@app.put("/clientes/{id}")
def editar_cliente(id:int, datos_cliente: Cliente):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes[i] = datos_cliente
            return {"mensaje": "Cliente actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
@app.delete("/clientes/{id}")
def eliminar_cliente(id:int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            del lista_clientes[i]
            return {"mensaje": "Cliente eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")   


















@app.get("/facturas")
def listar_facturas():
    return lista_facturas  


@app.post("/facturas")
def crear_facturas(datos_facturas: Factura):
    lista_facturas.append(datos_facturas)
    return {"factura": datos_facturas}