from rest_framework.serializers import ModelSerializer
from projectmanager.models import Contributor, Project, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "password"]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        project = super().create(validated_data)
        user = self.context["request"].user
        # Add User as main contributor of this project
        Contributor.objects.create(
            user=user,
            project=project,
            role='creator',
        )
        return project


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'role']


class ContributorListUserSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user']
