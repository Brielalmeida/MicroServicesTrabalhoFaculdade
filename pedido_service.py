import json
from fastapi import FastAPI

app = FastAPI()

@app.post("/pedido/{user_id}/add")
async def cadastrar_pedidos(user_id: int):
    pedido = {"status" : "criado", "order_id" : user_id}
    pedido_json = json.dumps(pedido)
    try:
        with open("./database/pedidos.txt", "a") as file:
            file.write(f"{pedido_json}\n")
    except Exception as e:
        return {"message": f"Erro ao escrever no arquivo: {e}"}
    return {"message": "Pedido criado com sucesso!"}

@app.get("/pedido")
async def ver_pedidos():
   return _carregar_pedidos()
    
@app.get("/pedido/{order_id}")
async def buscar_pedido_por_id(order_id: int):
    return _buscar_pedido_por_id(order_id)

def _carregar_pedidos() -> dict :
    try:
        with open("./database/pedidos.txt", "r") as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return {"message" : "Arquivo não criado"}

def _buscar_pedido_por_id(order_id: int) -> dict:
    try:
        with open("./database/pedidos.txt", "r") as file:
            pedidos = [json.loads(line) for line in file]
            pedidos_iguais = [pedido for pedido in pedidos if pedido["order_id"] == order_id]
            if pedidos_iguais:
                return pedidos_iguais
            else:
                return {"message": "Pedido não encontrado"}
    except FileNotFoundError:
        return {"message": "Arquivo não criado"}
    
