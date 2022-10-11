
import requests

base_url = "https://sandbox.leantech.me"
lean_token = '43a5e5ab-4403-43dc-a1f5-dbb9420ab803'


# Create Payment Intent


def cre_payment_intent(cust_id, amt, currency):
    url = base_url+"/payments/v1/intents/"
    payload = {
        "customer_id": cust_id,
        "amount": amt,
        "currency": currency,
        "description": "Testing first time"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lean-app-token": lean_token
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text) # "payment_intent_id":"874bd862-2b38-4dd8-883b-adf92b42300f"


# cust_id = '51bcaa7f-7b24-40c6-a639-47caaf46aa02'
# amt = '1000'
# currency = 'AED'
# cre_payment_intent(cust_id, amt, currency)

# Get Payment Intent
def get_payment_intent(pay_intid):
    url = base_url+f"/payments/v1/intents/{pay_intid}"
    url = "https://sandbox.leantech.me/payments/v1/intents/874bd862-2b38-4dd8-883b-adf92b42300f/"

    headers = {
        "accept": "application/json",
        "lean-app-token": lean_token
    }

    response = requests.get(url, headers=headers)

    print(response.text)
    
pay_intid='874bd862-2b38-4dd8-883b-adf92b42300f'
get_payment_intent(pay_intid)