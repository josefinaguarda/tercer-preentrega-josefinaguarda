#from django.shortcuts import render


#def home(request):
    #return render(request, "core/index.html")

from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')