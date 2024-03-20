from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/produtos")
async def listar_produtos():
    return _carregar_produtos()

@app.post("/produtos/{id}/{nome}/{preco}")
async def cadastrar_produtos(id: int, nome: str, preco: float):
    produto = {"id":id,"nome": nome, "preco": preco}
    produto_json = json.dumps(produto)
    try:
        with open("./database/produtos.txt", "a") as file:
            file.write(f"{produto_json}\n")
    except Exception as e:
        return {"message": f"Erro ao escrever no arquivo: {e}"}
    return {"message": "Produto cadastrado com sucesso!"}

def _carregar_produtos() -> dict :
    try:
        with open("./database/produtos.txt", "r") as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return {"message" : "Arquivo não criado"}