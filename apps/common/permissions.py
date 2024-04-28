from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'admin':
            return True
        return False


class IsTecherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'teacher' or 'admin':
            return True
        return False