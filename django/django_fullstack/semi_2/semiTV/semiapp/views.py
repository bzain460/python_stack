from django.db.models.base import ModelStateFieldsCacheDescriptor
from semiapp.models import TV, add_show
from django.shortcuts import redirect, render, render_to_response
from django.contrib import messages
from . import models

def index(request):
    return render(request,'index.html')

def add(request):
    errors = TV.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Title=request.POST['title']
        Network=request.POST['net']
        Release_date=request.POST['release']
        Description=request.POST['desc']
        x = add_show(Title,Network,Release_date,Description)
        y = x.id
        return redirect('show/' + str(y))

def show(request, id):
    context={
        'current_show':TV.objects.get(id=id),
        'id' : id
    }
    return render(request, 'tv_show.html',context)

def delete(request, id):
    x = TV.objects.get(id=id)
    x.delete()
    return redirect('/allshows')



def edit(request, id):
    context={
        'current_show':TV.objects.get(id=id),
        'id' : id
    }
    return render(request,'editshow.html',context)


def editprocess(request, id):
    y = id
    errors = TV.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/show/'+str(y)+'/edit')
    else:
        x = TV.objects.get(id=id)
        print(x.Title)
        x.Title = request.POST['title']
        x.Network = request.POST['net']
        x.Description = request.POST['desc']
        x.Release_date = request.POST['rel']
        x.save()
        messages.success(request, "Blog successfully updated")
        return redirect('/show/'+str(y))


def allshows(request):
    context = {
        'shows' : TV.objects.all()
    }
    return render(request, 'Allshow.html' ,context)