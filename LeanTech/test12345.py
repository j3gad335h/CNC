import requests

url = "https://sandbox.sa.leantech.me/payments/v1/intents/e26f8038-9e4a-456e-88d9-78cb325c0bfd"

headers = {
    "accept": "application/json",
    "lean-app-token": "961f2078-1356-4755-8b22-4dcc16d02a50"
}

response = requests.get(url, headers=headers)

print(response.text)