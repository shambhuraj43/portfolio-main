from django.urls import path
from resume_section import views

app_name = 'resume_section'

resume_sections = [
        {
            "resume_section":"education",
            "view":"education"
        },
        {
            "resume_section":"professional-experience",
            "view":"professional_experience"
        },
                {
            "resume_section":"publications",
            "view":"publications"
        },
                {
            "resume_section":"leadership",
            "view":"leadership"
        },
                {
            "resume_section":"skills",
            "view":"skills"
        },
                {
            "resume_section":"projects",
            "view":"projects"
        }
    ]

urlpatterns = [
    path('resume/', views.resume_page, name='resume_page'),
    path('resume/education', views.education, name='education'),
    path('resume/professional_experience', views.professional_experience, name='professional_experience'),
    path('resume/publications', views.publications, name='publications'),
    path('resume/leadership', views.leadership, name='leadership'),
    path('resume/skills', views.skills, name='skills'),
    path('resume/projects', views.projects, name='projects'),
]