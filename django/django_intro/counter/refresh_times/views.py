from django.shortcuts import render

def refresh(request):
    if 'refresh'in request.session:
        request.session['refresh']=request.session['refresh']+1
    else:
        request.session['refresh']=1
    # Create your views here.
    context = {
        "counter" : request.session['refresh']
    }
    return render(request,'index.html',context)

def destroy(request):
    request.session.clear()
    request.session.pop('refresh', None)
    return render(request,'index.html')