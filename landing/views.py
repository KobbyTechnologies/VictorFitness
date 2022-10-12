from email import message
from django.shortcuts import redirect, render
from . models import Program, Program_Detail, Topic, ProgramAttachments
from customer.models import SubscriptionFeatures, SubscriptionPlan
from workouts.models import ProgramWorkout
from django.contrib import messages

# Create your views here.


def landing(request):
    Program_Name = Program.objects.all()
    pkg = SubscriptionPlan.objects.all().order_by('price')
    workout = ProgramWorkout.objects.all()

    ctx = {
        "ProgName": Program_Name,
        'pkg': pkg,
        'workout': workout,
    }
    return render(request, 'main/landing.html', ctx)

def landing_alt(request):
    Program_Name = Program.objects.all()
    pkg = SubscriptionPlan.objects.all().order_by('price')
    workout = ProgramWorkout.objects.all()

    ctx = {
        "ProgName": Program_Name,
        'pkg': pkg,
        'workout': workout,
    }
    return render(request, 'main/index.html', ctx)


def about(request):
    return render(request, 'main/about.html')


def programs(request):
    programs = Program_Detail.objects.all()
    tabs = Program.objects.all()
    ctx = {"pro": programs, "tab": tabs}
    return render(request, 'main/programs.html', ctx)


def programsDetails(request, pk):
    programs = Program_Detail.objects.get(id=pk)
    topic = Topic.objects.filter(program=pk)
    attach = ProgramAttachments.objects.filter(program=pk)

    ctx = {"pro": programs, "topic": topic, "attach": attach}
    return render(request, 'main/Details.html', ctx)
