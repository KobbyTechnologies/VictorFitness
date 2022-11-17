from django.shortcuts import render
from landing import models
from workouts import models


#### Create your views here ##########

def payment(request, plan_id):
    # planDetail = models.Program_Detail.objects.get(pk=plan_id)
    workouts = models.ProgramWorkout.objects.get(pk=plan_id)
    return render(request, 'payment.html', {'workout': workouts})
    # {'res':planDetail}, 



def checkout_session(request, plan_id):
    pass

