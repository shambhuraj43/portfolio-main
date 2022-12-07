from django.urls import path
from landing_page import views

app_name = 'landing_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('generic/', views.generic, name='generic'),
    path('generic/', views.generic, name='generic'),
    path('elements/', views.elements, name='elements'),
]