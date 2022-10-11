import requests

base_url = 'https://sandbox.leantech.me'
lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'


def list_banks():
    url = base_url+"/banks/v1/"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }
    response = requests.get(url, headers=headers)

    print(response.text)

list_banks()