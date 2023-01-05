from django.urls import path
from project_page import views
from graphene_django.views import GraphQLView
from .schema import schema

app_name = 'project_page'

urlpatterns = [
    path('project/<str:project_id>', views.index, name='project_page'),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]