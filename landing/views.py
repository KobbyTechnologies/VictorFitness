from django.shortcuts import redirect, render
from . models import Program

# Create your views here.
def landing (request):
    Program_Name = Program.objects.all()
    # if request.method == 'POST':
    #     weight = int(request.POST['weight'])
    #     height = int(request.POST['height'])
    #     if height >0 and weight > 0:
    #         res = height/3.281
    #         BMI = weight/(res*res)
    #         new_bmi= round(BMI,3)
    #         if new_bmi < 18.5:
    #             myBMI = (f"your BMI is: {new_bmi} and you're in the underweight range")
    #         elif new_bmi >18.5 and new_bmi <=24.9:
    #             myBMI = (f"your BMI is: {new_bmi} and you're in the healthy weight range")
    #         elif new_bmi >=25 and new_bmi <=29.9:
    #             myBMI=(f"your BMI is: {new_bmi} and you're in the overweight range")
    #         else:
    #             myBMI = (f"your BMI is: {new_bmi} and you're in the obese range")
    #     else:
    #         myBMI= ("Invalid Entry")
    # ctx = {"BMI":myBMI}
    ctx = {"ProgName":Program_Name}
    return render (request, 'main/landing.html',ctx)
def about (request):
    return render (request, 'main/about.html')
