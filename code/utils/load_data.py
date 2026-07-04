import json
#----------------------------------------------------------------
# Lee un fichero JSON
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
#----------------------------------------------------------------
# Se cargan los distintos ficheros necesarios para la ejecucion del experimento
def load_data_files(params_path, api_keys_path, scenarios_path):
      print("Cargando parámetros...", end = " ")
      params = load_json(params_path)
      api_keys = load_json(api_keys_path)
      print("[OK]")

      print("Cargando dataset...", end = " ")
      data_scenarios = load_json(scenarios_path) 
      print("[OK]")
      return params, api_keys, data_scenarios
