import requests

lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'
base_url = 'https://sandbox.sa.leantech.me'


# Create Customer

def create_customer(cust_name):
    payload = {"app_user_id": cust_name}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }
    url = base_url+"/customers/v1"
    response = requests.post(url, json=payload, headers=headers)
    # {"customer_id":"b8283759-c7f3-4d94-9346-4812b8bde4d2","app_user_id":"jegadeesh_test1"}
    print(response.text)

# Get Customer by app_user_id

def get_cust_details(app_user_id):
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }
    url = base_url+f"/customers/v1/app-user-id/{app_user_id}/"
    response = requests.get(url, headers=headers)
    print(response.text)


create_customer("jegadeesh_test1_sa")
get_cust_details('jegadeesh_test1')
