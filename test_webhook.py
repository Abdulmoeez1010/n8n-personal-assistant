import requests

user_message = "Tell me about us iran war. Like a summary type"

request_message = {
    "message": user_message}

response = requests.post("http://localhost:5678/webhook-test/d68a4117-c039-43f7-8f71-1c135a727d1e", json=request_message)
print(response.status_code)
print(response.json())