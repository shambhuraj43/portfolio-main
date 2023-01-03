from django.shortcuts import render


def index(request, project_id):

    context = {
        "project_name": "PROJECT_NAME",
        "project_description": "PROJECT_DESCRIPTION",
        "technolgies_used": [
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon":'docker'
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon":"none"
            },
            {
                "name": "docker",
                "description": "TECHNOLOGY DESCRIPTION",
                "icon":"none"
            },
        ],
        "installation_requirements": "INSTALLATION REQUIREMENTS",
        "requirements_file":"Requirements.txt",
        "requirements_file_link":"https://github.com/shambhuraj43/portfolio-main",
        "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
    }
    return render(request, f"project_page/{project_id}.html", context)
