import graphene
from graphene_django import DjangoObjectType

from .models import Project

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ("id", "project_name", "project_description", "requirements_file", "requirements_file_link", "github_repo_link")


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

schema = graphene.Schema(query=Query)