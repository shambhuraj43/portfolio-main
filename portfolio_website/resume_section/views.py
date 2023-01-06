from django.shortcuts import render, redirect
from config import projects_context
# Create your views here.


def resume_page(request):
    return render(request, "resume_section/base.html", projects_context)


def education(request):
    response = redirect('http://127.0.0.1:8000/resume/#education')
    return response


def professional_experience(request):
    response = redirect(
        'http://127.0.0.1:8000/resume/#professional_experience')
    return response


def publications(request):
    response = redirect('http://127.0.0.1:8000/resume/#publications')
    return response


def leadership(request):
    response = redirect('http://127.0.0.1:8000/resume/#leadership')
    return response


def skills(request):
    response = redirect('http://127.0.0.1:8000/resume/#skills')
    return response


def projects(request):
    response = redirect('http://127.0.0.1:8000/resume/#projects')
    return response
