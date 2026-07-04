from google import genai
from google.genai import types

# Llama a la API de Gemini con los parametros necesarios y el prompt a evaluar
def run_gemini(api_key, model_name, params, prompt):
	client = genai.Client(api_key=api_key)
    
	response = client.models.generate_content(
		model = model_name,
		contents = prompt,
		config = types.GenerateContentConfig(
			temperature = params["temperature"],
			#top_p = params["top_p"],
			max_output_tokens = params["max_output_tokens"]
		)
	)

	return response.text
