from email import message
from django.shortcuts import redirect, render
from . models import Program, Program_Detail, Topic, ProgramAttachments
from django.contrib import messages

# Create your views here.


def landing(request):
    Program_Name = Program.objects.all()

    ctx = {"ProgName": Program_Name}
    return render(request, 'main/landing.html', ctx)


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
