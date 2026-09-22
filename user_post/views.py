from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Students
def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")

        if name == "" or age == "" or city == "":
            return render(request, "signup.html", {"error":"All fields are required"})
        elif Students.objects.filter(name=name).exists():
            return render(request, "signup.html", {"error":"User already exists"})
        form = Students(name=name,age=age, city=city)
        form.save()
    return render(request, "signup.html", {"name":"peter"})


def login(request):
    return render(request, "pages/login.html")



def profile(request):
    student= Students.objects.all()
    return render(request, "profile.html", {"users":student })