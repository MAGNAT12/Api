import requests

# response = requests.get("http://127.0.0.1:3000/api/user")
# print(response.status_code)
# print(response.json())

data = {
    "name": "Magnat",
    "gmail": "rizamatmu@gmail.com"
}

response = requests.post("http://127.0.0.1:3000/api/users", data=data)
print(response.json())

