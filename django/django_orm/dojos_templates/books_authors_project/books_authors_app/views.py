from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):
    context = {"dojos": models.Dojo.objects.all()}
    return render(request,'index.html',context)

def add_dojo(request):
    newly_created_dojo = models.Dojo.objects.create(name=request.POST['name'],
    City=request.POST['city'],State=request.POST['state'])
    return redirect("/")

def add_ninja(request):
    this_dojo=models.Dojo.objects.get(id=request.POST['select'])
    newly_created_ninja = models.Ninga.objects.create(first_name=request.POST['first_name'],
    last_name=request.POST['last_name'],dojo=this_dojo)
    return redirect ("/")