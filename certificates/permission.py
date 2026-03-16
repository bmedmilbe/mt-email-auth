from rest_framework.permissions import BasePermission
from .models import Customer
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and bool(Customer.objects.get(user_id=request.user.id, backstaff=True))
