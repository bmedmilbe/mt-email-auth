# middleware.py
from django.shortcuts import get_object_or_404
from models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Identify tenant from Header (cleanest for APIs)
        tenant_id = request.headers.get('X-Tenant-ID')
        
        if tenant_id:
            request.tenant = get_object_or_404(Tenant, id=tenant_id)
        else:
            request.tenant = None
            
        response = self.get_response(request)
        return response