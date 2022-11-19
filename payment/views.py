from django.shortcuts import render,redirect
from django.urls import reverse
from landing import models
from workouts import models
from customer import models
from myRequest.api.lipaNaMpesa import lipa_na_mpesa

def payment(request, pkg_id):

    pkg = models.SubscriptionPlan.objects.get(pk=pkg_id)
    # plans = models.PersonalPlan.objects.get(pk=pkg_id)
    if request.method == 'POST':
        try:
            phone_number = request.POST.get('phone_number')
            amount = 1
            account_reference = "Victor Fitness"
            transaction_desc = request.POST.get('transaction_description')
            callback_url =  request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
            response = lipa_na_mpesa(amount,phone_number,callback_url, account_reference, transaction_desc)
            print(response)
            return redirect("payment",pkg_id=pkg_id)
        except Exception as e:
            print(e)
            return redirect("payment",pkg_id=pkg_id)
    context = {
        'pkg': pkg,
        # 'plans': plans,
        "pkg_id":pkg_id
    }
    return render(request, 'payment.html', context)





