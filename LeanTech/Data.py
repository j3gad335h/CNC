
from unittest import result
import requests
import json

base_url = "https://sandbox.leantech.me"
lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'

# Get Accounts


def get_accounts(ent_id):
    url = base_url+"/data/v1/accounts/"
    payload = {"entity_id": ent_id}

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

# Get Balance


def get_balance(account_id, entity_id):
    url = base_url+"/data/v1/balance/"

    payload = {
        "account_id": account_id,
        "entity_id": entity_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

# Get Identity


def get_identity(entity_id):
    url = base_url+"/data/v1/identity/"

    payload = {"entity_id": entity_id}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

# Get Transactions


def get_transactions(entity_id, account_id):
    url = base_url+"/data/v1/transactions/"

    payload = {
        "entity_id": entity_id,
        "account_id": account_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

# Name Verification


def name_verification(entity_id, full_name):
    url = base_url+"/insights/v1/name-verification/"

    payload = {
        "entity_id": entity_id,
        "full_name": full_name
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    json_dict = json.loads(response.text)
    return json_dict.get('results_id')


def verification_result(res_id):
    url = base_url+f"/data/v1/results/{res_id}/"

    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)
    print(response.text)


entity_id = 'd5f36c08-2564-3295-86ea-7e339aea58be'
account_id = 'dc0fd58c-b1e3-4663-a0dd-57fafcf7514c'
get_accounts(entity_id)
print("------")
get_balance(account_id,
            entity_id)
print("------")
get_identity(entity_id)
print("------")
get_transactions(entity_id, account_id)
print("------")
res = name_verification(entity_id, 'Michael Garry Scott')
verification_result(res)
print("------")
res = name_verification(entity_id, 'Gonzalo Thiel')
verification_result(res)
