from email.policy import default
from genericpath import exists
from logging import exception
import os
from re import U
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserInfo, Gallery,Workout,Goals
from datetime import date, datetime
from django.template.loader import get_template
from django.template import Context
from io import BytesIO
from xhtml2pdf import pisa
from landing.models import Program_Detail,Program
from dateutil.relativedelta import relativedelta
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def Customer(request):
    return render(request,"customer.html")

@login_required(login_url='login')
def CustomerLibrary(request):
    programs=''
    try:
        programs = Program_Detail.objects.filter(price="Paid") 
    except:
        pass
    ctx = {"pro":programs}
    return render(request,"library.html",ctx)


@login_required(login_url='login')
def CustomerProfile(request):
    exits =''
    BMI = ''
    genders = ''
    dateOfBirth =''
    profilePic = ''
    WHR=''
    BFP = ''
    difference_in_years= ''
    try:
        exits = UserInfo.objects.get(names=request.user)
        today =date.today()
        dob = exits.date_of_birth
        time_difference = relativedelta(today, dob)
        difference_in_years = int(time_difference.years)
    except:
        pass
    
    try:
        obj= Workout.objects.filter(user=request.user).latest('date_added')
        BMI = round (obj.weight/((obj.height/100)**2),2)
        WHR = round((obj.waist/obj.hip),2)
        if exits.gender == 'Male' or exits.gender == 'Other':
            BFP = round(1.20 * obj.bmi + 0.23 * difference_in_years-16.2,2)
        elif exits.gender == 'Female':
            BFP = round(1.20 * obj.bmi + 0.23 * difference_in_years-5.4,2)
        else:
            BFP = 0
    except:
        pass  
    ctx={"info": exits,"bmi":BMI,"whr":WHR,
         "age":difference_in_years,"BFP":BFP}
    return render(request,"customerProfile.html",ctx)

def userInfo(request):
    exits = ''
    try:
        exits = UserInfo.objects.get(names=request.user)
    except:
        pass
    if request.method == 'POST':
        try:
            sex = request.POST.get('gender')
            contact = request.POST.get('contact')
            dateOfBirth= datetime.strptime(request.POST.get('date_of_birth'), '%Y-%m-%d').date()
            profilePic = request.FILES['profilePic']
        except:
            pass
        if sex == '0':
            genders = 'Male'
        if sex == '1':
            genders = 'Female'
        if sex== '2':
            genders = 'Other'
        if exits:
            exits.contacts =contact
            exits.gender =genders
            exits.date_of_birth =dateOfBirth
            exits.profilePic =profilePic
            exits.save()
            messages.success(request, "successfully Updated")
            return redirect('customerProfile')
        if not exits:
            user_obj = UserInfo.objects.create(
                names = request.user,
                contacts = contact,
                gender=genders,
                date_of_birth  = dateOfBirth,
                profilePic = profilePic,
            )
            messages.success(request, "successfully Added")
            return redirect('customerProfile')
    return redirect ('customerProfile')
    

@login_required(login_url='login')
def Gallery_Request(request):
    if request.method == "POST":
        try:
            pic = request.FILES.getlist('addPhoto')
        except exception as e:
            print("Invalid attachment")
            return redirect('gallery')
        for file in pic:
            myAlbum = Gallery.objects.create(
                pic=file,
                user = request.user,
            )
        return redirect('gallery')
    album = Gallery.objects.filter(user=request.user) 
    ctx = {"album":album}
    return render(request,"gallery.html",ctx)
def workout(request):
    target = ''
    try:
        sex= UserInfo.objects.get(names=request.user)
        gender = sex.gender
    except:
        pass
    if request.method == "POST":
        try:
            weight = int(request.POST.get('weight'))
            height = int(request.POST.get('height'))
            waist = int(request.POST.get('waist'))
            hip = int(request.POST.get('hip'))
        except:
            pass
        try:
            BMI = (round (weight/((height/100)**2),2)) 
            target1 = (round (18.5 * ((height / 100) ** 2)))
            target2 = (round (24.9 * ((height / 100) ** 2)))
            
            # WHR START
            WHR = round((waist/hip),2)
            if waist > 0 and hip > 0:          
                if gender  == 'Male' or gender == 'Other':
                    if WHR > 1:
                        whrStatus = 'High'
                        whrs = WHR
                    elif WHR >= 0.96 and WHR >=1.0:
                        whrStatus = 'Moderate' 
                        whrs = WHR
                    elif WHR <= 0.96:
                        whrStatus = 'Low'
                        whrs = WHR
                    else:
                        whrStatus = 'Invalid Entries'
                if gender  == 'Female':
                    if WHR > 0.85:
                        whrStatus = 'High'
                        whrs = WHR
                    elif WHR >= 0.81 and WHR >=0.85:
                        whrStatus = 'Moderate' 
                        whrs = WHR
                    elif WHR <= 0.81:
                        whrStatus = 'Low'
                        whrs = WHR
                    else:
                        whrStatus = 'Invalid Entries'
            else:
                whrTarget = 'Hip and waist cannot be negative.'
            # WHR END
            # BMI START
            if BMI > 29.9:
                status = 'Obese'
                target = f'Your target weight is between: {target1} and {target2}'
            elif BMI >=24.9 and BMI <=29.9:
                status = 'Overweight'
                target = f'Your target weight is between: {target1} and {target2}'
            elif BMI >=18.5 and BMI <24.9:
                status = 'Health'
                target = 'You are doing Good'
            elif BMI >=1 and BMI <18.5:
                status = 'Underweight'
                target = f'Your target weight is between: {target1} and {target2}'
            else:
                status = "Invalid Entries"
            # BMI END
        except :
            pass
        
        workouts =Workout.objects.create(
            weight=weight,
            height=height,
            user=request.user,
            bmi = BMI,
            status = status,
            recommendations = target,
            waist =waist,
            hip = hip,
            whr = whrs,
            whrStatus =whrStatus,
        )
        messages.success(request, "successfully Added")
        return redirect ('customerProfile')
    return redirect ('customerProfile')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def my_view(request):
    try:
        obj= Workout.objects.filter(user=request.user)
        obj2= Goals.objects.filter(user=request.user)
        obj3 = UserInfo.objects.get(names=request.user)
        objs= Workout.objects.filter(user=request.user).latest('date_added')
        today =date.today()
        dob = obj3.date_of_birth
        time_difference = relativedelta(today, dob)
        difference_in_years = int(time_difference.years)
        
        if obj3.gender == 'Male' or obj3.gender == 'Other':
            BFP = 1.20 * objs.bmi + 0.23 * difference_in_years-16.2
        if obj3.gender == 'Female':
            BFP = 1.20 * objs.bmi + 0.23 * difference_in_years-5.4
        if request.method == "POST":
            return render_to_pdf(
                'stats.html',
                {
                    'data': obj,
                    'name':request.user,
                    'goals':obj2,
                    'Age':difference_in_years,
                    'BFP':BFP,
                }
            )
    except:
        pass
def WorkoutGoals(request):
    if request.method == "POST":
        try:
            goals = request.POST.get('goals')
        except:
            pass
        obj = Goals.objects.create(
            goals=goals,
            user=request.user
        )
        messages.success(request, "successfully Added")
        return redirect ('customerProfile')
    return redirect ('customerProfile')
