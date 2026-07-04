import os, time
from datetime import datetime
from llm_clients.gemini_client import run_gemini
from llm_clients.openai_client import run_openai
from llm_clients.claude_client import run_claude
from utils.results import save_md, save_results_json, build_result
from utils.load_data import load_data_files
from convert_scenarios import export_scenarios_to_json

# Directorios de salida
RESULTS_MD_DIR = "results/results_md"
RESULTS_JSON_DIR = "results/json"
# Rutas a la configuracion de los modelos y parametros
PARAMS_PATH = "config/params.json"
API_KEYS_PATH = "config/api_keys.json"
# Ruta al dataset de escenarios
SCENARIOS_PATH = "data/data_scenarios.json"

#export_scenarios_to_json("data/escenarios.xlsx",SCENARIOS_PATH)

# Se crean las carpetas principales de resultados en caso de que no existan
os.makedirs(RESULTS_MD_DIR, exist_ok=True)
os.makedirs(RESULTS_JSON_DIR, exist_ok=True)

# Carga de datos y parametros
params, api_keys, data_scenarios = load_data_files(PARAMS_PATH, API_KEYS_PATH, SCENARIOS_PATH)
GEMINI_API_KEY = api_keys["GEMINI_API_KEY"]
OPENAI_API_KEY = api_keys["OPENAI_API_KEY"]
CLAUDE_API_KEY = api_keys["CLAUDE_API_KEY"]

# Definición del modelo de lenguaje
MODEL_NAME_GEMINI = "gemini-3-flash-preview"
MODEL_NAME_OPENAI = "gpt-5.4"
MODEL_NAME_CLAUDE = "claude-sonnet-4-6"

# Contador para evitar esperar en la ejecución del último escenario
remaining_scenarios = len(data_scenarios)
# Se inicializa la variable resultados para almacenar en JSON
results = []
# Se obtiene el timestamp de ejecución del experimento y se eliminan los ":" y "T"
run_timestamp = datetime.now().isoformat(timespec="seconds").replace(":", "").replace("T","_")

# Se recorren los escenarios del JSON para su ejecución en el modelo
for scenario in data_scenarios:
	scenario_id = scenario['id']
	scenario_rol = scenario['rol']
	prompt = scenario["prompt"].strip()

	print(f"Ejecutando escenario {scenario_id} ...")
	# Se obtiene el timestamp de respuesta de cada escenario
	response_timestamp = datetime.now().isoformat(timespec="seconds").replace(":", "").replace("T","_")

	# Ejecución del modelo
	print("Ejecutando Gemini ...")
	response_text_gemini = run_gemini(GEMINI_API_KEY, MODEL_NAME_GEMINI, params, prompt)
	print("Ejecutando OpenAI ...")
	response_text_openai = run_openai(OPENAI_API_KEY, MODEL_NAME_OPENAI, params, prompt)
	print("Ejecutando Claude ...")
	response_text_claude = run_claude(CLAUDE_API_KEY, MODEL_NAME_CLAUDE, params, prompt)
	
	md_filename_gemini = f"scenario{scenario_id}_{scenario_rol}_{MODEL_NAME_GEMINI}_{response_timestamp}.md"
	md_filename_openai = f"scenario{scenario_id}_{scenario_rol}_{MODEL_NAME_OPENAI}_{response_timestamp}.md"
	md_filename_claude = f"scenario{scenario_id}_{scenario_rol}_{MODEL_NAME_CLAUDE}_{response_timestamp}.md"
	
	# Guardar respuesta de LLM en fichero MD, creando una subcarpeta por cada escenario
	md_path_gemini = f"{RESULTS_MD_DIR}/scenario_{scenario_id}/{md_filename_gemini}"
	md_path_openai = f"{RESULTS_MD_DIR}/scenario_{scenario_id}/{md_filename_openai}"
	md_path_claude = f"{RESULTS_MD_DIR}/scenario_{scenario_id}/{md_filename_claude}"

	save_md(md_path_gemini, response_text_gemini)
	save_md(md_path_openai, response_text_openai)
	save_md(md_path_claude, response_text_claude)

	# Se crea el formato de cada resultado en JSON para su almacenamiento
	result_gemini = build_result(response_timestamp, MODEL_NAME_GEMINI, scenario, md_filename_gemini,
								   prompt, response_text_gemini)

	result_openai = build_result(response_timestamp, MODEL_NAME_OPENAI, scenario, md_filename_openai,
								   prompt, response_text_openai)
	
	result_claude = build_result(response_timestamp, MODEL_NAME_CLAUDE, scenario, md_filename_claude,
								   prompt, response_text_claude)

	# Se añaden los resultados de cada LLM a la lista de resultados y se guarda en un JSON
	results.extend([result_gemini, result_openai, result_claude])
	results_json_path = f"{RESULTS_JSON_DIR}/results_{run_timestamp}.json"
	save_results_json(results_json_path, results)
	
	# Si no es el último escenario, espero 1 minuto para no saturar la API
	remaining_scenarios -= 1
	if remaining_scenarios > 0:
		print("Esperando 60 segundos hasta próxima ejecución...")
		time.sleep(60)
	
print("ESCENARIOS FINALIZADOS")
