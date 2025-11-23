from rest_framework_nested import routers
from . import views  

router = routers.DefaultRouter()

router.register("flights", views.FlightsViewSet, basename="flights")
router.register("enquires", views.EnquireViewSet, basename="enquires")
router.register("trushs", views.TrushsViewSet, basename="trushs")


urlpatterns = (router.urls)




# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
