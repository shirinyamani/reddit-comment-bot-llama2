import requests
import json 


    
def call_llama(prompt, model='llama2', stream=False):
    url = 'http://localhost:11434/api/generate'
    data = {
        'model': model,
        'prompt': prompt,
        'stream': stream
    }
    json_data = json.dumps(data)
    
    response = requests.post(url=url, data=json_data, headers={'Content-Type': 'application/json'})
    
    try:
        response_json = response.json()
        return response_json
    except json.JSONDecodeError:
        # Handle the case where the response is not JSON (e.g., error message)
        return None