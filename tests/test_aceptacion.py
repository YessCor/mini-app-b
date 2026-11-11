from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)
def test_pagina_principal():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "text/html" in respuesta.headers["content-type"]


def test_lista_de_cinco_preguntas():
    preguntas = cliente.get("/api/preguntas").json()
    assert len(preguntas) == 5
    for pregunta in preguntas:
        assert isinstance(pregunta["id"], int)
        assert pregunta["texto"]
        assert len(pregunta["opciones"]) == 4


def test_no_revela_la_respuesta():
    for pregunta in cliente.get("/api/preguntas").json():
        assert set(pregunta) == {"id", "texto", "opciones"}


def test_responder_correcta_e_incorrecta():
    pregunta = cliente.get("/api/preguntas").json()[0]
    primera = cliente.post("/api/responder", json={"id": pregunta["id"], "opcion":
    0})
    correcta = primera.json()["respuesta_correcta"]
    assert 0 <= correcta <= 3
    acierto = cliente.post("/api/responder", json={"id": pregunta["id"], "opcion":
    correcta})
    assert acierto.json()["correcta"] is True
    otra = (correcta + 1) % 4
    fallo = cliente.post("/api/responder", json={"id": pregunta["id"], "opcion":
    otra})
    assert fallo.json()["correcta"] is False


def test_pregunta_inexistente():
    respuesta = cliente.post("/api/responder", json={"id": 9999, "opcion": 0})
    assert respuesta.status_code == 404


def test_opcion_fuera_de_rango():
    pregunta = cliente.get("/api/preguntas").json()[0]
    respuesta = cliente.post("/api/responder", json={"id": pregunta["id"], "opcion":
    7})
    assert respuesta.status_code == 422