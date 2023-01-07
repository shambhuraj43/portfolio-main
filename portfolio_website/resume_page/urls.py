from django.urls import path
from resume_page import views

urlpatterns = [
    path('new_resume', views.index, name="index")
]