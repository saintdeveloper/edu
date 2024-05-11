from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'admin':
            return True
        return False


class IsTecherAndAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status in ['admin', 'teacher']:
            return True
        return False