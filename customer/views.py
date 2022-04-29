from logging import exception
from re import U
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import UserInfo, Gallery

# Create your views here.

@login_required(login_url='login')
def Customer(request):
    return render(request,"customer.html")

@login_required(login_url='login')
def CustomerProfile(request):
    info= UserInfo.objects.get(names=request.user)
    ctx={"info": info}
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


