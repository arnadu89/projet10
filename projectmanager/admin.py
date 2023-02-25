from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from projectmanager.models import *


admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Comment)
admin.site.register(Issue)
