from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectmanager.models import Contributor, Project, User


admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Contributor)
