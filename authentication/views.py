from django.shortcuts import render,redirect
from django.urls import reverse
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from .models import MyUser
from django.conf import settings
import threading

# Create your views here.

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)                                                                     

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[user.email]
                         )

    EmailThread(email).start()
        
def register_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if len(password) < 6:
            messages.error(request,'Password should be at least 6 characters')
            return redirect('register')
        if password != password2:
            messages.error(request,'Password mismatch')
            return redirect('register')
        if not validate_email(email):
            messages.error(request, 'Enter a valid email address')
            return redirect('register')
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        if MyUser.objects.filter(username=username).exists():
            messages.error(request,  'Username is taken, choose another one')
            return redirect('register')
        if MyUser.objects.filter(email=email).exists():
            messages.error(request,'Email is taken, choose another one')
            return redirect('register')
        try:
            user = MyUser.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            send_activation_email(user, request)
            messages.success(request,'We sent you an email to verify your account')
            return redirect('login')
        except Exception as e:
            print (e)
            messages.error(request,e)
            return redirect('register')         
    return render(request,'accounts/register.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user and not user.is_email_verified:
            messages.error(request,'Email is not verified, please check your email inbox')
            return redirect('login')
        if not user:
            messages.error(request, 'Invalid credentials, try again')
            return redirect('login')
        try:
            login(request, user)
            return redirect('customer')
        except  Exception as e:
            print(e)
            messages.error(request, e)
           
        
    return render(request, 'accounts/login.html')

def logout_request(request):
    logout(request)
    return redirect('landing')

def activate_user(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = MyUser.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.success(request,'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'activate-failed.html', {"user": user})

