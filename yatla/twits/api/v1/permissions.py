from rest_framework import permissions


class IsAuthenticatedOnCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        # For creation requests, POST, requires authentication
        if request.method == "POST":
            return request.user and request.user.is_authenticated
        return True


class IsAuthenticatedOnTimeLine(permissions.BasePermission):
    def has_permission(self, request, view):
        # For creation requests, POST, requires authentication
        if view.action == "timeline":
            return request.user and request.user.is_authenticated
        return True
