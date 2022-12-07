from django.urls import path
from signup_section import views

app_name = 'signup_section'

urlpatterns = [
    path('signup/', views.index, name='index'),
]