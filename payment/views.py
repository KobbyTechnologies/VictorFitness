from django.shortcuts import render,redirect
from landing import models
from workouts import models
from django_daraja.mpesa.core import MpesaClient


cl = MpesaClient()
stk_push_callback_url = 'https://darajambili.herokuapp.com/express-payment'

def payment(request, plan_id):
    # planDetail = models.Program_Detail.objects.get(pk=plan_id)
    workouts = models.ProgramWorkout.objects.get(pk=plan_id)
    return render(request, 'payment.html', {'workout': workouts,"plan_id":plan_id})
def stk_push(request,plan_id):
    if request.method == 'POST':
        try:
            token = cl.access_token()
            print(token)
            phone_number = request.POST.get('phone_number')
            amount = int(request.POST.get('amount'))
            account_reference = "Shape and Tone"
            transaction_desc = request.POST.get('transaction_description')

            callback_url = stk_push_callback_url
            r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            print(r.json())
            return redirect("payment",plan_id=plan_id)
        except Exception as e:
            print(e)
            return redirect("payment",plan_id=plan_id)
    return redirect("payment",plan_id=plan_id)

def checkout_session(request, plan_id):
    pass

