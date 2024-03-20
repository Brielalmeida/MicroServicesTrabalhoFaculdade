import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/logins")
async def listar_login():
    return _carregar_login()

@app.post("/login/new/{id}/{username}/{password}")
async def cadastrar_login(id: int, username: str, password: str):
    cliente = {"id":id,"username": username, "password": password}
    cliente_json = json.dumps(cliente)
    try:
        with open("./database/login.txt", "a") as file:
            file.write(f"{cliente_json}\n")
    except Exception as e:
        return {"message": f"Erro ao escrever no arquivo: {e}"}
    return {"message": "Login cadastrado com sucesso!"}

def _carregar_login() -> dict :
    try:
        with open("./database/login.txt", "r") as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return {"message" : "Arquivo não criado"}
