from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class TenantEmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not request or not hasattr(request, 'tenant'):
            return None

        # Try to find user where (email OR phone) matches the input 
        # AND belongs to the current tenant identified by middleware
        try:
            user = User.objects.get(
                (Q(email=username) | Q(phone=username)) & 
                Q(tenant=request.tenant)
            )
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None