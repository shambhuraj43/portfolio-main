from django.urls import path
from resume_section import views

urlpatterns = [
    path('resume/', views.resume_page, name='resume_page'),
]