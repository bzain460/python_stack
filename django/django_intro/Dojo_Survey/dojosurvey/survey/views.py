from django.shortcuts import render
def hani(request):
    return render(request,"index.html")
        
def karmel(request):
    
    name = request.POST['txt']
    location = request.POST['loc']
    language = request.POST['lang']
    comment = request.POST['tex']
    context = {
    	"name" : name,
    	"location" : location,
    	"language":language,
    	"comment":comment
    }
    return render(request,"result.html",context)

