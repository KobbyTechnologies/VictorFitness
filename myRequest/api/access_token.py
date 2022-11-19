import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings as config


def generate_access_token():
    consumer_key = config.MPESA_CONSUMER_KEY
    consumer_secret = config.MPESA_CONSUMER_SECRET
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)
        
    json_response = (r.json())  

    my_access_token = json_response["access_token"]

    return my_access_token
generate_access_token()