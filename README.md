## Alineamiento normativo de LLMs en la gestión y notificación de incidentes TIC según DORA

Este repositorio contiene el código fuente desarrollado para el Trabajo Fin de Estudio del Máster Universitario en Inteligencia Artificial de la Universidad Internacional de La Rioja (UNIR).
El proyecto evalúa el grado de alineamiento de distintos modelos de lenguaje con los requisitos de resiliencia operativa digital establecidos por DORA, en el contexto de la gestión de incidentes TIC en el sector financiero.

El experimento ejecuta escenarios simulados de incidentes de ciberseguridad sobre distintos modelos de lenguaje y almacena sus respuestas para su posterior evaluación mediante una rúbrica definida.

### Modelos evaluados

- claude-sonnet-4.6
- gpt-5.4
- gemini-3-flash-preview

### Datasets

Los escenarios simulados se encuentran en el fichero `data/data_scenarios.json`

### Ejecución

python main.py

### Resultados

Los resultados se almacenan automáticamente en la carpeta `results/`
Se generan dos tipos de ficheros:
- Ficheros Markdown con la respuesta de cada modelo.
- Fichero JSON con todos los resultados de la ejecución del experimento.
