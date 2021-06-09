from semiapp.models import TV, add_show
from django.shortcuts import redirect, render, render_to_response
from . import models

def index(request):
    return render(request,'index.html')

def add(request):
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
    
    x = TV.objects.get(id=id)
    print(x.Title)
    x.Title = request.POST['titleup']
    x.Network = request.POST['netup']
    x.Description = request.POST['descup']
    x.Release_date = request.POST['relup']
    x.save()
    z = x.id
    return redirect('/show/'+str(z))


def allshows(request):
    context = {
        'shows' : TV.objects.all()
    }
    return render(request, 'Allshow.html' ,context)