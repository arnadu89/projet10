from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from projectmanager.serializers import ProjectSerializer, UserSerializer
from projectmanager.models import Project, User


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class ProjectListView(ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectUserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return User.objects.filter(contributor__project_id=project_id)

    def post(self, request, *args, **kwargs):
        # Récupérer les informations du request.post
        # créer l'objet contributor avec le bon serializer
        return self.create(request, *args, **kwargs)
