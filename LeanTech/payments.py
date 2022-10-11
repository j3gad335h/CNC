
import requests

base_url = "https://sandbox.leantech.me"
lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'

# Get all Payment Sources for Customer
url = "https://sandbox.leantech.me/customers/v1/beb7697d-d0f2-4ec7-b169-af3700822235/payment-sources/"

headers = {
    "accept": "application/json",
    "lean-app-token": "43a5e5ab-4403-43dc-a1f5-dbb9420ab803"
}

response = requests.get(url, headers=headers)

print(response.text)


def cust_payment_source(cust_id):
    url = base_url+"/customers/v1/{cust_id}/payment-sources/"

    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)

    print(response.text)


cust_payment_source('b8283759-c7f3-4d94-9346-4812b8bde4d2')