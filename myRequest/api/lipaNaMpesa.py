import requests
from myRequest.api.access_token import generate_access_token
from myRequest.api.encode import generate_password
from myRequest.api.utils import get_timestamp
from django.conf import settings as config
# Create your views here.

def lipa_na_mpesa(Amount,phone_number,CallBackURL,AccountReference,TransactionDesc):
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": config.BUSINESS_SHORTCODE,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": Amount,
        "PartyA": phone_number,
        "PartyB": config.MPESA_EXPRESS_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": CallBackURL,
        "AccountReference": AccountReference,
        "TransactionDesc": TransactionDesc,
    }
    response = requests.post(api_url, json=request, headers=headers)

    return response.json()
