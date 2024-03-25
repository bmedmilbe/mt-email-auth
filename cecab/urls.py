from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet

router = routers.DefaultRouter()

router.register("associations", views.AssociationViewSet, basename="associations")
router.register("bands", views.BandViewSet, basename="bands")
router.register("spots", views.SpotViewSet, basename="spots")
router.register("yeargols", views.YearGolsViewSet, basename="yeargols")
router.register("posts", views.PostViewSet, basename="posts")
router.register("postview", views.PostViewViewSet, basename="postview")
router.register("messages", views.MessagesViewSet, basename="messages")
router.register("postimage", views.PostImagesViewSet, basename="postimages")
router.register("teams", views.TeamViewSet, basename="teams")
router.register("pathners", views.PathnerViewSet, basename="pathners")




posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(
    r"postimages", views.PostImagesViewSet, basename="post-postimages"
)


urlpatterns = (
    router.urls
    + posts_router.urls
   
)


# router.register("customers", views.CustomersViewSet, basename='customers')


# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
