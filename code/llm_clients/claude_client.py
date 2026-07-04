import anthropic

# Llama a la API de Anthropic con los parámetros necesarios y el prompt a evaluar
def run_claude(api_key, model_name, params, prompt):	
	client = anthropic.Anthropic(api_key=api_key)

	response = client.messages.create(
		model = model_name,
		max_tokens = params["max_output_tokens"],
		temperature = params["temperature"],
		#top_p = params["top_p"],
		messages = [
			{ "role": "user",
			  "content": prompt }
		]
	)

	return response.content[0].text