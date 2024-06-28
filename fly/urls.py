from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet

router = routers.DefaultRouter()

# router.register("airports", views.AirportViewSet, basename="airports")
# router.register("countries", views.CountryViewSet, basename="countries")
# router.register("flight", views.FlightViewSet, basename="flight")
router.register("enquires", views.EnquireViewSet, basename="enquires")



# tours_router = routers.NestedSimpleRouter(
#     router, r"tours", lookup="tour")
# tours_router.register(r"images", views.ImagesTourViewSet,
#                          basename="tour-images")


# services_router = routers.NestedSimpleRouter(
#     router, r"services", lookup="service")
# services_router.register(r"informations", views.InformationViewSet,
#                          basename="service-information")


urlpatterns = (
    router.urls
    # + tours_router.urls
    # + services_router.urls
    # + orders_router.urls
    # + carts_router.urls
    # + shopmanages_router.urls
    # + shops_router.urls
    # + customers_router.urls
    # + delivers_router.urls
)


# router.register("customers", views.CustomersViewSet, basename='customers')


# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
