from django.views.generic import TemplateView
from django.urls import path
from . import views


urlpatterns = [
    # path('', TemplateView.as_view(template_name='core/index.html'))
    # path('password/', views.PasswordViewSet, basename="password"),

    path('core/email', views.say_hello, name="email"),
    # path('core/myaddress', views.my_address, name="my-address"),
    path('core/myaddress', views.my_address, name="my-address"),
    
]
