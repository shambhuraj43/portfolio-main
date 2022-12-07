from django.urls import path
from resume_section import views

app_name = 'resume_section'

urlpatterns = [
    path('resume/', views.resume_page, name='resume_page'),
]