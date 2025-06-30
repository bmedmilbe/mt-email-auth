from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet

router = routers.DefaultRouter()

router.register("posts", views.PostViewSet, basename="posts")
router.register("fronts", views.FrontViewSet, basename="fronts")

router.register("postview", views.PostViewViewSet, basename="postview")
router.register("sections", views.SectionViewSet, basename="sections")
router.register("tours", views.TourViewSet, basename="tours")
router.register("services", views.ServiceViewSet, basename="services")
router.register("messages", views.MessagesViewSet, basename="messages")

# router.register("postimage", views.PostImagesViewSet, basename="postimages")
router.register("teams", views.TeamViewSet, basename="team")
router.register("assemblys", views.AssemblyViewSet, basename="assembly")

# posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
# posts_router.register(
#     r"postimages", views.PostImagesViewSet, basename="post-postimages"
# )

tours_router = routers.NestedSimpleRouter(
    router, r"tours", lookup="tour")
tours_router.register(r"images", views.ImagesTourViewSet,
                         basename="tour-images")


services_router = routers.NestedSimpleRouter(
    router, r"services", lookup="service")
services_router.register(r"informations", views.InformationViewSet,
                         basename="service-information")


urlpatterns = (
    router.urls
    + tours_router.urls
    + services_router.urls
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
