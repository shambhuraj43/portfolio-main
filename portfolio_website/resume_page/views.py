from django.shortcuts import render
from django.http import HttpResponse
from config import projects_context

# Create your views here.
def index(request):
    return render(request, "resume_page/base.html", {"projects":projects_context})
