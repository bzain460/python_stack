from django.shortcuts import render

# Create your views here.
def index(request):
    ha = {
        'name': 'khalil'
    }
    return render(request, 'index.html', ha)

