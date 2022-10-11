import requests
base_url = "https://sandbox.sa.leantech.me"
lean_token = '961f2078-1356-4755-8b22-4dcc16d02a50'


def get_cust_payment_dest(cust_id):
    url = base_url+f"/customers/v1/{cust_id}/payment-destinations/"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)

    print(response.text)


def get_payment_dest():
    url = base_url+f"/payments/v1/destinations/"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)

    print(response.text)


def get_payment_dest_id(pay_dest_id):
    url = base_url+f"/payments/v1/destinations/{pay_dest_id}"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)

    print(response.text)


def cre_payment_dest():
    url = "https://sandbox.leantech.me/payments/v1/destinations/"
    payload = {
        "bank_identifier": "ENBD_UAE",
        "branch_address": "45 Lansing Street, Dubai, United Arab Emirates",
        "name": "Jegadeesh N",
        "iban": "AE870200000XXXXXXXXXXX1",
        "display_name": "Jegadeesh N",
        "address": "1234 Sky Bldg.",
        "city": "Abu Dhabi",
        "country": "ARE",
        "swift_code": "EBILAEADXXX",
        "account_number": "XXXXXXXXXXXX",
        "customer_id": "51bcaa7f-7b24-40c6-a639-47caaf46aa02"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": "43a5e5ab-4403-43dc-a1f5-dbb9420ab803"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


get_cust_payment_dest('51bcaa7f-7b24-40c6-a639-47caaf46aa02')  # Invalid Url
# get_payment_dest()
# get_payment_dest_id('23e7454f-a5ec-4f58-8ff4-136ef09f2257')
# cre_payment_dest()