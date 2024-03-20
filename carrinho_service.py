import json
from fastapi import FastAPI

app = FastAPI()

@app.post("/carrrinho/{user_id}/add/{produto_id}/{quantidade}")
async def cadastrar_carrinho(user_id: int, produto_id: int, quantidade:int):
    return _salvar_carrinho(user_id, produto_id, quantidade)

@app.get("/carrrinho/ver/{user_id}")
async def cadastrar_carrinho(user_id: int):
    return _carregar_carrinho(user_id)

def _salvar_carrinho(user_id: int, produto_id: int, quantidade:int):
    pedido = {"produto": produto_id, "quantidade": quantidade}
    path = f"./database/carrinho/user_{user_id}.txt"
    with open(path, "a") as file:
        file.write(json.dumps(pedido) + "\n")
    return {"message": "Item adicionado ao carrinho com sucesso!"}

def _carregar_carrinho(user_id: int) -> dict :
    try:
        path = f"./database/carrinho/user_{user_id}.txt"
        with open(path, "r") as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return {}