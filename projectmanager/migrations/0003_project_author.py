# Generated by Django 4.1.7 on 2023-02-23 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0002_project_issue_contributor_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
