from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from projectmanager.serializers import *
from projectmanager.models import Contributor, Project, User
from projectmanager.permissions import *


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectCreateSerializer
    list_serializer_class = ProjectListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(
            Q(contributor__user=user) | Q(author=user)
        )
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectListSerializer
    queryset = Project.objects.all()
    permission_classes = (IsAuthor, IsContributorReadOnly)


class ProjectContributorListCreateView(ListCreateAPIView):
    serializer_class = ContributorSerializer
    list_serializer_class = ContributorListUserSerializer
    permission_classes = (IsProjectAuthor,)

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


class ProjectContributorDeleteView(DestroyAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [IsProjectAuthor]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(user=user_id, project_id=project_id)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
