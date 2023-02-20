from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, ForeignKey


class User(AbstractUser):
    pass


class Project(models.Model):
    title = CharField(max_length=128)
    description = CharField(max_length=128)
    type = CharField(max_length=128)


class Contributor(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)
    role = CharField(max_length=128)


class Issue(models.Model):
    title = CharField(max_length=128)
    description = CharField(max_length=128)
    tag = CharField(max_length=128)
    priority = CharField(max_length=128)
    status = CharField(max_length=128)
    created_time = DateTimeField(auto_now_add=True)

    user = ForeignKey(User, on_delete=models.CASCADE)
    project = ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):
    description = CharField(max_length=128)
    created_time = DateTimeField(auto_now_add=True)

    user = ForeignKey(User, on_delete=models.CASCADE)
    issue = ForeignKey(Issue, on_delete=models.CASCADE)
