from email import message
from django.shortcuts import redirect, render
from . models import Program, Program_Detail,Topic,ProgramAttachments
from django.contrib import messages

# Create your views here.
def landing (request):
    Program_Name = Program.objects.all()
    status=""
    if request.method == 'POST':
        try:
            height=float( request.POST.get('height'))
            weight=float(request.POST.get('weight'))
            print(height,weight)
        except ValueError:
            print('invalid input')
            return redirect('landing')
            
        if (height>0) and (weight>0):
            BMI = weight // (height ** 2)
            if BMI< 18.5:
                status = 'Underweight'
            elif BMI <= 24.9:
                status = 'Healthy'
            elif BMI<= 29.9:
                status = 'Overweight'
            else:
                status ='obese '
        else:
            status= 'height and weight cannot be negative'
    print(status)
    ctx = {"ProgName":Program_Name, "status":status}
    return render (request, 'main/landing.html',ctx)


def about (request):
    return render (request, 'main/about.html')

def programs (request):
    programs = Program_Detail.objects.all() 
    tabs = Program.objects.all()
    ctx = {"pro":programs,"tab":tabs}
    return render (request, 'main/programs.html', ctx)
def programsDetails (request,pk):
    programs = Program_Detail.objects.get(id=pk) 
    topic = Topic.objects.filter(program=pk)
    attach = ProgramAttachments.objects.filter(program=pk)

    ctx = {"pro":programs,"topic":topic,"attach":attach}
    return render (request, 'main/Details.html', ctx)

