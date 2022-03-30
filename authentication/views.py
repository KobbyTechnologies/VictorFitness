from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def register_request(request):
    context={}
    if request.method == "POST":
        try:
            form=request.POST.get('data')
            if form.is_valid():
                form.save()
                messages.success(request, "Registration successful." )
                print("success")
                return redirect('login')
        except Exception as e:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            print(e)
        context['register_form']=form
    else:
        context['register_form']=form
    return render(request,'accounts/register.html',context)

def login_request(request):
    context={}
    if request.method == "POST":
        form=request.POST.get('data')
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect('post')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            context['login_form']=form
            messages.error(request,"Invalid username or password.")
    else:
        context['login_form']=form
    return render(request, 'accounts/login.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')

