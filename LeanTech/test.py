import requests

url = "https://sandbox.sa.leantech.me/customers/v1/a884d081-ff04-4812-bb38-ad6c9fdf13d8/entities/"

headers = {
    "accept": "application/json",
    "lean-app-token": "961f2078-1356-4755-8b22-4dcc16d02a50"
}

response = requests.get(url, headers=headers)

print(response.text)