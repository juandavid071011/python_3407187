from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente

app = FastAPI()

lista_clientes = []
lista_facturas = []


@app.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Cliente creado exitosamente", "cliente": datos_cliente}

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