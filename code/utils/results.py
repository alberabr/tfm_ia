import json, os
#----------------------------------------------------------------
# Guardar respuesta en un JSON
def save_results_json(results_json_path, results):
	with open(results_json_path, "w", encoding="utf-8") as f:
		json.dump(results, f, ensure_ascii = False, indent = 2)
	
	print(f"Resultados añadidos a: {results_json_path}")
	return
#----------------------------------------------------------------
# Guardar respuesta de LLM en fichero MD
def save_md(md_path, response_text):	
	# Se crea la subcarpeta de resultados si no existe	
	os.makedirs(os.path.dirname(md_path), exist_ok=True)
	with open(md_path, "w", encoding="utf-8") as f:
		f.write(response_text)

	print(f"Respuesta guardada en: {md_path}")
	return
#----------------------------------------------------------------
# Crea la estructura JSON en formato diccionario del resultado de una ejecucion
def build_result(timestamp, model_name, scenario, md_filename, prompt, response_text):
	return {
		"timestamp": timestamp,
		"model": model_name,	
		"scenario_id": scenario["id"],
		"scenario_type": scenario["tipo"],
		"rol": scenario["rol"],
		"md_file": md_filename,
		"prompt": prompt,
		"response": response_text
	}	
