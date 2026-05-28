import sys
import requests
import json

def call_local_llama(prompt):
    # Simplified prompt, no file-listing overhead to prevent server hang
    url = "http://127.0.0.1:8080/completion"
    payload = {
        "prompt": f"<|start_header_id|>system<|end_header_id|>\nYou are the Godhead Architect. Analyze security tasks.<|eot_id|><|start_header_id|>user<|end_header_id|>\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
        "n_predict": 128,
        "temperature": 0.1
    }
    try:
        response = requests.post(url, json=payload, timeout=30)
        return response.json()['content']
    except Exception as e:
        return f"Server is struggling: {e}"

def godhead_supervisor(user_input):
    return call_local_llama(user_input)

if __name__ == "__main__":
    query = " ".join(sys.argv[1:])
    print(godhead_supervisor(query))
