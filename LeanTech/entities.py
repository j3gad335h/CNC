import requests

# Get Entities
base_url = 'https://sandbox.leantech.me'
lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'


def get_entities(cust_id):
    url = base_url+f"/customers/v1/{cust_id}/entities"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)
    print(response.text)

# Get an entity by id


def get_entity_by_id(cust_id, ent_id):
    url = base_url+f"/customers/v1/{cust_id}/entities/{ent_id}"
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }
    response = requests.get(url, headers=headers)
    print(response.text)

# Delete Entity
    # Delete Entity doesnt work as expected in both from Py file as well as in sandbox test


def del_entity(cust_id, ent_id, reason):
    url = base_url+f"/customers/v1/{cust_id}/entities/{ent_id}"
    payload = {"reason": reason}
    headers = {
        "content-type": "application/json",
        "lean-app-token": lean_token
    }
    response = requests.delete(url, json=payload, headers=headers)
    print(response.text)


cust_id = '51bcaa7f-7b24-40c6-a639-47caaf46aa02'
ent_id = 'c9e27726-0962-3d04-9a55-fe096c95cd62'
print("----------------")
get_entities(cust_id)

print("----------------")
get_entity_by_id(cust_id, ent_id)

# print("----------------")
# del_entity(cust_id, 'c9e27726-0962-3d04-9a55-fe096c95cd62', "USER_REQUESTED")
