import pytest
from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_mejora_cantidad_tres_devuelve_tres_preguntas():
    respuesta = cliente.get("/api/preguntas?cantidad=3")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 3


@pytest.mark.parametrize("cantidad", [1, 3, 5])
def test_lista_la_cantidad_solicitada(cantidad):
    respuesta = cliente.get("/api/preguntas", params={"cantidad": cantidad})

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == cantidad


def test_cantidad_predeterminada_es_cinco():
    respuesta = cliente.get("/api/preguntas")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 5


def test_cantidad_aparece_en_la_documentacion_openapi():
    parametros = app.openapi()["paths"]["/api/preguntas"]["get"]["parameters"]

    cantidad = next(parametro for parametro in parametros if parametro["name"] == "cantidad")
    assert cantidad["in"] == "query"
    assert cantidad["required"] is False
    assert cantidad["schema"]["minimum"] == 1
    assert cantidad["schema"]["maximum"] == 5


@pytest.mark.parametrize("cantidad", [0, 6])
def test_cantidad_fuera_de_rango_responde_422(cantidad):
    respuesta = cliente.get("/api/preguntas", params={"cantidad": cantidad})

    assert respuesta.status_code == 422
