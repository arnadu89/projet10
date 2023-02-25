from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, ForeignKey, Q


class User(AbstractUser):
    def is_project_contributor(self, project_id):
        if Project.objects.filter(
            Q(contributor__user=self) | Q(author=self),
            id=project_id
        ):
            return True
        return False

    def is_project_author(self, project_id):
        if Project.objects.filter(
            author=self,
            id=project_id
        ):
            return True
        return False


class Project(models.Model):
    title = CharField(max_length=128)
    description = CharField(max_length=128)
    type = CharField(max_length=128)
    author = ForeignKey(User, on_delete=models.CASCADE)


class Contributor(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    role = CharField(max_length=128)

    class Meta:
        unique_together = ('user', 'project')


class Issue(models.Model):
    title = CharField(max_length=128)
    description = CharField(max_length=128)
    tag = CharField(max_length=128)
    priority = CharField(max_length=128)
    status = CharField(max_length=128)
    created_time = DateTimeField(auto_now_add=True)

    author = ForeignKey(User, on_delete=models.CASCADE, related_name="writed_issues")
    assignee = ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_issues")
    project = ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):
    description = CharField(max_length=128)
    created_time = DateTimeField(auto_now_add=True)

    author = ForeignKey(User, on_delete=models.CASCADE)
    issue = ForeignKey(Issue, on_delete=models.CASCADE)
