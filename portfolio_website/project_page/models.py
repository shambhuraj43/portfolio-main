from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=1000)
    project_description = models.CharField(max_length=1000)
    requirements_file = models.CharField(max_length=1000)
    requirements_file_link = models.CharField(max_length=1000)
    github_repo_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.project_name


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