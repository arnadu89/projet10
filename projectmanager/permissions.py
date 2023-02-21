from rest_framework import permissions


class IsContributor(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # if request.user.is_superuser:
        #     return True

        if request.user.is_project_contributor(obj.project):
            return True

        return False


class IsAuthorToUpdateOrContributorToReadOnly(IsContributor):
    def has_object_permission(self, request, view, obj):
        # if request.user.is_superuser:
        #     return True

        if not request.user.is_project_contributor(obj.project):
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_project_creator(obj.project):
            return True

        return False
