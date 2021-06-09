from django.http.response import HttpResponse
from django.shortcuts import render
import random


def index(request):
    return render(request, 'index.html')



def check(request, method = 'POST'):

    if 'num' not in request.session:
        request.session['num'] = random.randint(1, 100)

    num = int(request.session['num'])

    print(num)
    number_from_form = int(request.POST['usernum'])
    if number_from_form < num:
        return HttpResponse('<h1>The number is higher</h1>')
    if number_from_form > num:
        return HttpResponse('<h1>The number is lower</h1>')
    if number_from_form == num:
        return HttpResponse('<h1>Your Awnser Was Right!</h1>')
    
