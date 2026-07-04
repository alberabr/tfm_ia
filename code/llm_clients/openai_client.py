from openai import OpenAI

# Llama a la API de OpenAI con los parametros necesarios y el prompt a evaluar
def run_openai(api_key, model_name, params, prompt):	
	client = OpenAI(api_key=api_key)

	response = client.responses.create(
		model = model_name,
		input = prompt,
		temperature = params["temperature"],
		#top_p = params["top_p"],
		max_output_tokens = params["max_output_tokens"]
	)
	
	return response.output_text
	