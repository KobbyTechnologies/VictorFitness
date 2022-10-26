import requests
from django.shortcuts import render
from landing import models
from workouts import models
from customer import models


#### Create your views here ##########

def payment(request, pkg_id):

    pkg = models.SubscriptionPlan.objects.get(pk=pkg_id)

    context = {
        'pkg': pkg,
    }
    return render(request, 'payment.html', context)


def checkout_session(request, plan_id):
    pass


response = requests.request(
    "GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
    headers={'Authorization': 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ=='}
)
print(response.text.encode('utf8'))
