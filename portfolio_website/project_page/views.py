from django.shortcuts import render, redirect
from config import project_page_context


def base_page(request, project_id):
    return render(request, f"project_page/base.html", project_page_context[project_id])

def github_page(request, project_id):
    response = redirect(f"https://github.com/shambhuraj43/{project_id}")
    return response