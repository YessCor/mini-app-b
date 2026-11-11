from typing import TypedDict


class Pregunta(TypedDict):
    id: int
    texto: str
    opciones: list[str]
    respuesta_correcta: int


_PREGUNTAS: list[Pregunta] = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Cuál es la capital de Japón?",
        "opciones": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "respuesta_correcta": 2,
    },
    {
        "id": 3,
        "texto": "¿Quién pintó la Mona Lisa?",
        "opciones": [
            "Vincent van Gogh",
            "Pablo Picasso",
            "Claude Monet",
            "Leonardo da Vinci",
        ],
        "respuesta_correcta": 3,
    },
    {
        "id": 4,
        "texto": "¿Qué océano es el más grande de la Tierra?",
        "opciones": [
            "Atlántico",
            "Índico",
            "Pacífico",
            "Ártico",
        ],
        "respuesta_correcta": 2,
    },
    {
        "id": 5,
        "texto": "¿Cuál es el resultado de 9 × 7?",
        "opciones": ["56", "63", "72", "49"],
        "respuesta_correcta": 1,
    },
]


def obtener_preguntas(cantidad: int = 5) -> list[dict[str, int | str | list[str]]]:
    return [
        {
            "id": pregunta["id"],
            "texto": pregunta["texto"],
            "opciones": pregunta["opciones"],
        }
        for pregunta in _PREGUNTAS[:cantidad]
    ]


def evaluar_respuesta(pregunta_id: int, opcion: int) -> tuple[bool, int] | None:
    for pregunta in _PREGUNTAS:
        if pregunta["id"] == pregunta_id:
            respuesta_correcta = pregunta["respuesta_correcta"]
            return opcion == respuesta_correcta, respuesta_correcta
    return None
