from django.urls import path
from project_page import views

app_name = 'project_page'

urlpatterns = [
    path('project/<str:project_id>', views.index, name='index'),
]