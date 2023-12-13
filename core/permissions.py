from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # List views are seen only by authenticated
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Write permissions only to owner
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # List views are filtered in queryset
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Object permissions only to owner
        if request.user.is_staff:
            return True
        return obj.owner == request.user

# TODO: create permissions for individual views, if needed
