from rest_framework import permissions


class IsAuthenticatedOnCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        # For creation requests, POST, requires authentication
        if request.method == "POST":
            return request.user and request.user.is_authenticated
        return True


class IsAuthenticatedOnModification(permissions.BasePermission):
    def has_permission(self, request, view):
        # For creation requests, POST, requires authentication
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return request.user and request.user.is_authenticated
        return True


class IsOwnerOnModification(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # For creation requests, POST, requires authentication
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return request.user == obj.user
        return True


class IsAuthenticatedOnTimeLine(permissions.BasePermission):
    def has_permission(self, request, view):
        # For creation requests, POST, requires authentication
        if view.action == "timeline":
            return request.user and request.user.is_authenticated
        return True
