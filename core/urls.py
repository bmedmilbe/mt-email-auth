from django.urls import path
from . import views


urlpatterns = [
    path('metadata', views.UnifiedMetadataView.as_view(), name="unified-metadata"),
]
