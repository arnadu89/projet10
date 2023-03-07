from rest_framework.serializers import ModelSerializer, ValidationError
from projectmanager.models import Contributor, Issue, Project, User, Comment


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "password"]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserSimpleSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ContributorSerializer(ModelSerializer):
    user = UserSimpleSerializer()

    class Meta:
        model = Contributor
        fields = ['user']


class ProjectSimpleSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title']


class ProjectListSerializer(ModelSerializer):
    author = UserSimpleSerializer()
    contributors = ContributorSerializer(many=True, source="contributor_set")

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'contributors']


class ProjectUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'type',
        )


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type']


class ContributorCreateSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user']


class ContributorListUserSerializer(ModelSerializer):
    user = UserSimpleSerializer()

    class Meta:
        model = Contributor
        fields = ['user']


class IssueSerializer(ModelSerializer):
    project = ProjectSimpleSerializer()
    author = UserSimpleSerializer()
    assignee = UserSimpleSerializer()

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'created_time',
            'author',
            'assignee',
            'project'
        ]


class IssueSimpleSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title']


class IssueCreateSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'assignee']


class CommentSerializer(ModelSerializer):
    author = UserSimpleSerializer()
    issue = IssueSimpleSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'created_time',
            'author',
            'issue',
        ]

    def validate(self, attrs):
        """Check that the Issue id is coherent with project id"""
        project_id = self.context['request'].parser_context['kwargs']["project_id"]
        issue_id = self.context['request'].parser_context['kwargs']["issue_id"]
        if not Issue.objects.filter(
                project_id=project_id,
                id=issue_id,
        ).exists():
            raise ValidationError(
                f"The issue with id {issue_id} is not associated with the project with id {project_id}"
            )

        return attrs


class CommentCreateSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ['description']
