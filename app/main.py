from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.requests import Request

from app.servicios import evaluar_respuesta, obtener_preguntas

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


class RespuestaEntrada(BaseModel):
    id: int
    opcion: Annotated[int, Field(ge=0, le=3)]


@app.get("/")
def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/api/preguntas")
def listar_preguntas(cantidad: Annotated[int, Query(ge=1, le=5)] = 5):
    return obtener_preguntas(cantidad)


@app.post("/api/responder")
def responder(entrada: RespuestaEntrada):
    resultado = evaluar_respuesta(entrada.id, entrada.opcion)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    correcta, respuesta_correcta = resultado
    return {
        "correcta": correcta,
        "respuesta_correcta": respuesta_correcta,
    }
