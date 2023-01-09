from django.urls import path
from resume_page import views

app_name = 'resume_page'

urlpatterns = [
    path('', views.resume_page, name="resume_page"),
    path('education', views.education, name='education'),
    path('professional_experience', views.professional_experience, name='professional_experience'),
    path('publications', views.publications, name='publications'),
    path('leadership', views.leadership, name='leadership'),
    path('skills', views.skills, name='skills'),
    path('projects', views.projects, name='projects'),
]