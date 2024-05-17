import json
import requests

data = {
    'id': 1,
    "name": "Azamat",
    "gmail": "azamatmufd@gmail.com"
}

headers = {'Content-Type': 'application/json'}
response = requests.put("http://127.0.0.1:3000/api/render", data=json.dumps(data), headers=headers)

print(response.json())
