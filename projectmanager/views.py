from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from projectmanager.serializers import ContributorSerializer, ContributorListUserSerializer, ProjectSerializer, UserSerializer
from projectmanager.models import Contributor, Project, User
from projectmanager.permissions import IsAuthorToUpdateOrContributorToReadOnly, IsContributor


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class ProjectListView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsContributor]

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(contributor__user=user)
        return queryset


class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthorToUpdateOrContributorToReadOnly]


class ProjectUserListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return User.objects.filter(contributor__project_id=project_id)


class ProjectContributorListCreateView(ListCreateAPIView):
    serializer_class = ContributorSerializer
    list_serializer_class = ContributorListUserSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project=project_id)

    def get_serializer_class(self):
        if self.request.method == 'get':
            return self.list_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        serializer.save(project_id=project_id)


class ProjectContributorDeleteView(APIView):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthorToUpdateOrContributorToReadOnly]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(user=user_id, project_id=project_id)

    def delete(self, request, pk, **kwargs):
        contributor = self.get_queryset()
        contributor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
