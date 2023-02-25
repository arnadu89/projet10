from rest_framework.serializers import ModelSerializer
from projectmanager.models import Contributor, Issue, Project, User, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "password"]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'role']


class ContributorListUserSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class IssueCreateSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'assignee']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description']
