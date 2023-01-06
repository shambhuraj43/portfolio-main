from django.urls import path
from project_page import views
from graphene_django.views import GraphQLView
from .schema import schema

app_name = 'project_page'

urlpatterns = [
    path('projects/<str:project_id>', views.base_page, name='base_page'),
    path('projects/<str:project_id>', views.github_page, name='github_page'),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]