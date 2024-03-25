from rest_framework.permissions import BasePermission

class IsDeliver(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.deliver and request.user.is_authenticated)
