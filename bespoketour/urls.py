from rest_framework_nested import routers
from . import views 

router = routers.DefaultRouter(trailing_slash=False)

router.register("metadata", views.MetadataViewSet, basename="metadata")
router.register("customer", views.CustomerViewSet, basename="customer")
router.register("customertags", views.CustomerTagViewSet, basename="customertags")
router.register("mixtags", views.MixTagViewSet, basename="mixtags")

urlpatterns = router.urls