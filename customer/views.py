from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Customer(request):
    return render(request,"customer.html")

@login_required(login_url='login')
def CustomerProfile(request):
    return render(request,"customerProfile.html")