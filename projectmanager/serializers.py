from rest_framework.serializers import ModelSerializer
from projectmanager.models import Project, User


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
