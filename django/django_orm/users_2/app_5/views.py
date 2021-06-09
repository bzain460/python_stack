from django.shortcuts import render, redirect
from . models import user


def index(request):
    context = {
        "Allusers": user.object.all()



    }


def index(request):
    return render(request, 'index.html')


def new(request):
    if request.method == "POST":
        user.objects.create(
            first_name=request.POST["first"], last_name=request.POST["last"], email=request.POST["email"], age=request.POST["age"])
    return redirect("/")
# Create your views here.
