## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.

## Objetivo
Agregar la funcionalidad de mejora para que el endpoint GET /api/preguntas acepte un parámetro opcional llamado 'cantidad' (entre 1 y 5), devolviendo únicamente esa cantidad de preguntas[cite: 23]. Sin el parámetro debe devolver 5, y si recibe un valor fuera del rango, debe responder con el código de estado 422[cite: 23]. Asimismo, actualiza la interfaz de la página principal para permitir elegir cuántas preguntas se desean jugar[cite: 23].

## Contexto
Lee AGENTS.md y los archivos existentes en app/ y tests/. El contrato de las pruebas de aceptación anteriores (tests/test_aceptacion.py) no debe modificarse[cite: 13].

## Restricciones
- No modifiques ni borres tests/test_aceptacion.py.
- Crea una nueva prueba en tests/test_mejora.py que compruebe explícitamente el funcionamiento de la mejora[cite: 13].
- Usa solo las dependencias declaradas en requirements.txt.
- No uses base de datos ni archivos externos para guardar los datos.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que vas a modificar o crear y espera mi aprobación. Al terminar, resume brevemente qué hace cada archivo modificado o nuevo.

## Ejemplo
GET /api/preguntas?cantidad=3 devuelve una lista con exactamente 3 preguntas de cultura general.
GET /api/preguntas?cantidad=7 responde con el código de estado 422.

## Criterio de éxito
python -m pytest -v pasa todas las pruebas (tanto las de aceptación como las de la mejora en tests/test_mejora.py) y ruff check no reporta errores. Si después de 3 intentos las pruebas no pasan, detente y explica el problema[cite: 13].