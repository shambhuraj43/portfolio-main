from django.urls import path
from project_page import views

app_name = 'project_page'

urlpatterns = [
    path('projects/<str:project_id>', views.base_page, name='base_page'),
]