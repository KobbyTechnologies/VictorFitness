from email.policy import default
from genericpath import exists
from logging import exception
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
    try:
        exits = UserInfo.objects.get(names=request.user)
    except:
        pass
    if request.method == 'POST':
        try:
            sex = request.POST.get('gender')
            contact = request.POST.get('contact')
            dateOfBirth= datetime.strptime(request.POST.get('date_of_birth'), '%Y-%m-%d').date()
            profilePic = request.FILES.get('profilePic')
        except:
            pass
        if sex == '0':
            genders = 'Male'
        if sex == '1':
            genders = 'Female'
        if sex== '2':
            genders = 'Other'
        
        if exits:
            created = UserInfo.objects.update(
                contacts = contact,
                gender=genders,
                date_of_birth  = dateOfBirth,
                profilePic = profilePic,
            )
            print("successfully updated")
            return redirect('customerProfile')
        if not exits:
            created = UserInfo.objects.create(
                names = request.user,
                contacts = contact,
                gender=genders,
                date_of_birth  = dateOfBirth,
                profilePic = profilePic,
            )
            print("successfully Created")
            return redirect('customerProfile')
    try:
        obj= Workout.objects.filter(user=request.user).latest('date_added')
        BMI = (round (obj.weight/((obj.height/100)**2),2)) 
    except:
        pass  
    ctx={"info": exits,"bmi":BMI}
    return render(request,"customerProfile.html",ctx)

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
                    elif WHR >= 0.96 and WHR >=1.0:
                        whrStatus = 'Moderate' 
                    elif WHR <= 0.96:
                        whrStatus = 'Low'
                    else:
                        whrStatus = 'Invalid Entries'
                if gender  == 'Female':
                    if WHR > 0.85:
                        whrStatus = 'High'
                    elif WHR >= 0.81 and WHR >=0.85:
                        whrStatus = 'Moderate' 
                    elif WHR <= 0.81:
                        whrStatus = 'Low'
                    else:
                        whrStatus = 'Invalid Entries'
            else:
                whrTarget = 'Hip and waist cannot be negative.'
            # WHR END
            print(whrStatus)
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
            whr=WHR,
            whrStatus =whrStatus,
        )
        print("Created successfully")
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
        #Retrieve data or whatever you need
        if request.method == "POST":
            return render_to_pdf(
                'stats.html',
                {
                    'pagesize':'A4',
                    'data': obj,
                    'name':request.user,
                    'goals':obj2,
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
        print('Added successfully')
        return redirect ('customerProfile')
    return redirect ('customerProfile')