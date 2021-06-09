from django.shortcuts import render, HttpResponse,redirect
from time import localtime, strftime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities']=[]

    context = {
        "activities":request.session['activities']
    }    
    return render(request,"forms.html",context)

def process(request):
    activities = request.session['activities']
    date_time = strftime("%B %d, %Y %H:%M %p", localtime())
    gold = request.session['gold']
    place = request.POST['which_form']

    if "gold" in request.session:
        if request.POST['which_form'] == 'farm':
            current_gold = random.randint(10, 20)
            request.session['gold'] = request.session['gold'] + current_gold
            print(current_gold)
        elif request.POST['which_form'] == 'cave':
            current_gold = random.randint(5, 10)
            request.session['gold'] = request.session['gold'] + current_gold
            print(current_gold)
        elif request.POST['which_form'] == 'house':
            current_gold = random.randint(2, 5)
            request.session['gold'] = request.session['gold'] + current_gold
            print(current_gold)
        elif request.POST['which_form'] == 'casino':
            current_gold = random.randint(-50, 50)
            request.session['gold'] = request.session['gold'] + current_gold
            print(current_gold)

    if current_gold >= 0:
        text = f"Earned {current_gold} golds from the {place}! ({date_time})"
            
    else:
        text = f"Entered a casino and lost {current_gold}...Ouch.. ({date_time})"
            
    activities.append(text)
    request.session['activities'] = activities         
    return redirect("/")

def destroy(request):
    request.session.flush()
    return redirect("/")