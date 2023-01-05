from django.shortcuts import render


def base_page(request, project_id):

    context = {
        "portfolio": {
            "project_name": "PROJECT_NAME",
            "project_description": "PROJECT_DESCRIPTION",
            "technolgies_used": [
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": 'docker'
                },
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": "none"
                },
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": "none"
                },
            ],
            "installation_requirements": [
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
            ],
            "requirements_file": "Requirements.txt",
            "requirements_file_link": "https://github.com/shambhuraj43/portfolio-main",
            "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
        },
        "django-rest-api": {
            "project_name": "PROJECT_NAME",
            "project_description": "PROJECT_DESCRIPTION",
            "technolgies_used": [
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": 'docker'
                },
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": "none"
                },
                {
                    "name": "docker",
                    "description": "TECHNOLOGY DESCRIPTION",
                    "icon": "none"
                },
            ],
            "installation_requirements": [
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
                {
                    "req": "PYTHON",
                           "version": "VERSION"
                },
            ],
            "requirements_file": "Requirements.txt",
            "requirements_file_link": "https://github.com/shambhuraj43/portfolio-main",
            "github_repo_link": "https://github.com/shambhuraj43/portfolio-main"
        }
    }
    return render(request, f"project_page/base.html", context[project_id])
