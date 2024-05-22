import json
import requests

headers = {'Content-Type': 'application/json'}
def put():
    data = {
        "id": 2,
        "name": "",
        "gmail": ""
    }

    response = requests.put("http://127.0.0.1:3000/api/render", data=json.dumps(data), headers=headers)

    print(response.json())

def post():
    date = {
        "name":"Azamat",
        "gmail":"azamat@gmail.com"
    }

    respons = requests.post("http://127.0.0.1:3000/api/users", data=json.dumps(date), headers=headers)
    print(respons.json())


def get():
    respons = requests.get("http://127.0.0.1:3000/api/user")
    print(respons.json())


def delet():
    payload = {'id': 1}
    response = requests.delete("http://127.0.0.1:3000/api/del", params=payload)
    print(response.json())

delet()