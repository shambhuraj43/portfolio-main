from django.shortcuts import render

# Create your views here.
def index(request, project_id):
    s = f"<h1>Project Name:{project_id}<h1>"
    # return HttpResponse(s)
    context = {
        "project_name":"PROJECT_NAME",
        "project_description":"PROJECT_DESCRIPTION",
        "technolgies_used":[
            {"name":"TECHNOLGY_NAME"},
            {"description":"TECHNOLOGY DESCRIPTION"},
        ],
        "installation_requirements":"INSTALLATION REQUIREMENTS",
        "github_repo_link":"GITHUB REPO LINK"
    }
    return render(request, f"project_page/{project_id}.html", context)

