from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "landing_page/index.html")

def generic(request):
    return render(request, 'landing_page/generic.html')

def elements(request):
    return render(request, 'landing_page/elements.html')
    
