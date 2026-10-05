from django.shortcuts import render
from django.http import HttpResponse
from .forms import Users_dataForm
from random import randint
from django.core.mail import send_mail
# Create your views here.
from .utils import hash_password, check_password_valid
from .models import Users_data
def register(request):
    if request.method == "POST":
        form = Users_dataForm(request.POST)
        if form.is_valid():
            users = form.save(commit=False) #pass= 123
            otp = randint(1000, 9999) # Generate a random ID
            send_mail("OTP Verification", f"Your OTP is: {otp}", "reviewmaster36@gmail.com", [users.email])
            users.password = hash_password(users.password) #sadksfwoe
            users.save()
            return HttpResponse("User registered successfully")
    return render(request, "register.html", {"form": Users_dataForm()})

def login(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Users_data.objects.get(email=email)
            if check_password_valid(password, user.password):
                request.session['user_id'] = user.id
                return HttpResponse("Login successful")
            else:
                return HttpResponse("Invalid password")
        except Users_data.DoesNotExist:
            return HttpResponse("User does not exist")
       
    return render(request, "login.html")

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        
    return HttpResponse("Logged out successfully")