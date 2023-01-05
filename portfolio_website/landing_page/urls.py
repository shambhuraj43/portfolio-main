from django.urls import path
from landing_page import views

app_name = 'landing_page'
urlpatterns = [
    path('', views.index, name='index'),
]