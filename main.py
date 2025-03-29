from fastapi import FastAPI
from pydantic import BaseModel
from bot import buscar_processos

app = FastAPI()

class Consulta(BaseModel):
    cpf: str

@app.post("/consulta")
async def consultar_processo(data: Consulta):
    resultado = await buscar_processos(data.cpf)
    return {"cpf": data.cpf, "resultados": resultado}
