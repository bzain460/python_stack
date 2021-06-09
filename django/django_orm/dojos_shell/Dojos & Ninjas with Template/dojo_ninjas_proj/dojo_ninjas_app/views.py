from django.shortcuts import render, HttpResponse, redirect
from .models import dojos,ninjas

def index(request):

    context = {
        "dojos": dojos.objects.all(),
        "ninjas": ninjas.objects.all(),
        }
    return render(request,"index.html",context)


def dojo_process(request):
    dojos.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return redirect("/")


def ninja_process(request):
    ninjas.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],dojo=dojos.objects.get(id=int(request.POST['dojo'])))
    return redirect("/")

def delete(request):
    dojos.objects.get(id=int(request.POST['del'])).delete()
    return redirect("/")