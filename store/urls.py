
from rest_framework_nested import routers
from . import views  
from django.urls import path

router = routers.DefaultRouter()


router.register("products", views.ProductViewSet, basename="products")
router.register("identities", views.IdentityViewSet,
                basename="identities")
router.register("orders", views.OrderViewSet,
                basename="orders")


# titles_router = routers.NestedSimpleRouter(router, r"titles", lookup="title")
# titles_router.register(
#     r"model", views.CertificateModelViewSet, basename="title-models")


urlpatterns = (
    router.urls

    # + titles_router.urls
    # + sub_collection_router.urls
    # + shop_router.urls
)
# ) + [path('itemsinshop/<str:cart_id>/', views.get_product_in_shop)]


# router.register("customers", views.CustomersViewSet, basename='customers')


# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
