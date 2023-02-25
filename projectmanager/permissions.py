from rest_framework import permissions


class IsProjectContributor(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False

        project_id = view.kwargs["project_id"]
        if request.user.is_project_contributor(project_id):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs["pk"]
        if not request.user.is_project_contributor(project_id):
            return False

        if request.method in permissions.SAFE_METHODS:
            return True


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # if request.user.is_superuser:
        #     return True

        return obj.author == request.user


class IsProjectAuthor(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False

        project_id = view.kwargs["project_id"]
        if request.user.is_project_author(project_id):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        project_id = view.kwargs["project_id"]
        if request.user.is_project_author(project_id):
            return True

        return False
