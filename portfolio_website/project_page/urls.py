from django.urls import path
from project_page import views

app_name = 'project_page'

urlpatterns = [
    path('project/', views.index, name='index'),
]