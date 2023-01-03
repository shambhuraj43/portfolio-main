from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, project_id):
    s = f"<h1>Project Name:{project_id}<h1>"
    # return HttpResponse(s)
    return render(request, "project_page/base_project_page.html")

