from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, project_id):
    s = f"<h1>Project Name:{project_id}<h1>"
    # return HttpResponse(s)
    context = {
        "project_name":"PROJECT_NAME",
        "project_description":"PROJECT_DESCRIPTION",
        "technolgies_used":[
            {"technology_name":"TECHNOLGY_NAME"},
        ]
    }
    return render(request, f"project_page/{project_id}.html", context)

