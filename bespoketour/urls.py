from rest_framework_nested import routers
from . import views 

router = routers.DefaultRouter(trailing_slash=False)

router.register("metadata", views.MetadataViewSet, basename="metadata")

urlpatterns = router.urls