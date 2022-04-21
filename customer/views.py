from re import U
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserInfo

# Create your views here.
@login_required(login_url='login')
def Customer(request):
    return render(request,"customer.html")

@login_required(login_url='login')
def CustomerProfile(request):
    info=UserInfo.objects.get(names=request.user) 
    ctx={"info": info}
    return render(request,"customerProfile.html" ,ctx)