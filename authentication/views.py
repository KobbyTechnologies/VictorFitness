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
