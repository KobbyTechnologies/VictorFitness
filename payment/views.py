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
