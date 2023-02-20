from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectmanager.models import Project, User


admin.site.register(User, UserAdmin)
admin.site.register(Project)
