from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """Custom permission to only allow owners of an object to edit it"""

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner


class IsModerator(BasePermission):
    """Класс для проверки модератора"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()