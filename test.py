import json
import requests

data = {
    "name": "",
    "gmail": ""
}

headers = {'Content-Type': 'application/json'}
response = requests.put("http://127.0.0.1:3000/api/render", data=json.dumps(data), headers=headers)

print(response.json())
