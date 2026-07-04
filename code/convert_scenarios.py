import pandas as pd

# Convierte los escenarios de Excel a JSON
def export_scenarios_to_json(xlsx_path, json_path):
    print("Convirtiendo escenarios de Excel a JSON...", end = " ")
    # Se lee el excel como un diccionario
    df = pd.read_excel(xlsx_path)
    # Se transforma en formato JSON
    df.to_json(json_path, orient = "records", force_ascii = False, indent = 2)
    print("[OK]")

    return

#export_scenarios_to_json("data/escenarios.xlsx","data/data_scenarios.json")