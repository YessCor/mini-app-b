## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con
pytest.
## Objetivo
Construir la mini-aplicación web [Trivia de cultura general] con estos requisitos:
1. GET / muestra una página que presenta las preguntas una por una, con cuatro
botones de opción, indica si la respuesta fue correcta y muestra el puntaje
acumulado.
2. GET /api/preguntas devuelve una lista de 5 preguntas de cultura general. Cada
pregunta tiene los campos id (entero), texto (texto) y opciones (lista de 4 textos).
La respuesta correcta no se incluye.
3. POST /api/responder recibe {"id": 1, "opcion": 2}, donde opcion es un índice de 0
a 3, y devuelve {"correcta": true o false, "respuesta_correcta": índice de 0 a 3}.
4. Si el id no existe, responde con el código 404. Si la opción no está entre 0 y 3,
responde con el código 422.
## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los
nombres de los campos y los códigos de estado deben coincidir con esas pruebas.
## Restricciones
- Usa solo las dependencias de requirements.txt.
- Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar
FastAPI en servicios.
- Guarda los datos en memoria, sin base de datos ni archivos.
- No modifiques tests/test_aceptacion.py.
- La página usa HTML, CSS y JavaScript sin librerías externas.
## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que
vas a crear y espera mi aprobación. Al terminar, resume en una línea qué hace cada
archivo.
## Ejemplo
GET /api/preguntas devuelve:
[{"id": 1, "texto": "¿Cuál es el planeta más grande del sistema solar?", "opciones":
["Marte", "Júpiter", "Saturno", "Venus"]}, ...]
POST /api/responder con {"id": 1, "opcion": 1} devuelve:
{"correcta": true, "respuesta_correcta": 1}
## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Si
después de 3 intentos las pruebas no pasan, detente y explica el problema.