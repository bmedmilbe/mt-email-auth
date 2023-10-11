from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet
from django.urls import path

router = routers.DefaultRouter()


router.register("countries", views.CountrysViewSet, basename="countries")
router.register("universities", views.UniversitysViewSet,
                basename="universities")
router.register("buildings", views.BiuldingTypeViewSet,
                basename="buildings")
router.register("cemiterios", views.CemiteriosViewSet,
                basename="cemiterios")
router.register("streets", views.StreetsViewSet, basename="streets")
router.register("changes", views.ChangesViewSet, basename="changes")
router.register("towns", views.TownViewSet, basename="towns")
router.register("countys", views.CountysViewSet, basename="countys")

router.register("titles", views.CertificateTitleViewSet, basename="title")
router.register("certificates",
                views.CertificateViewSet, basename="certificates")

router.register("customers", views.CustomerViewSet,
                basename="customers")
router.register("persons", views.PersonViewSet, basename="persons")
router.register("birthadddress", views.PersonBirthAddressViewSet,
                basename="birthadddress")
router.register("house", views.HouseViewSet, basename="house")
router.register("covalsetup", views.CovalSetUpViewSet, basename="covalsetup")
router.register("parents", views.ParentViewSet, basename="parents")


router.register("idtypes", views.IdTypeViewSet, basename="idtypes")
router.register("intituitions", views.InstituitionsViewSet,
                basename="intituitions")


customers_router = routers.NestedSimpleRouter(
    router, r"customers", lookup="customer")
titles_router = routers.NestedSimpleRouter(router, r"titles", lookup="title")
titles_router.register(
    r"model", views.CertificateModelViewSet, basename="title-models")
titles_router.register(
    r"person", views.CertificatePersonsViewSet, basename="title-persons")
titles_router.register(
    r"singleperson", views.CertificateSinglePersonsViewSet, basename="title-singlepersons")
titles_router.register(
    r"parent", views.CertificateSimpleParentsViewSet, basename="title-parents")
titles_router.register(
    r"date", views.CertificateDatesViewSet, basename="title-dates")
# customers_router.register(r"parcels", views.ParcelsViewSet, basename="customer-parcels")
# customers_router.register(r"fligths", views.FligthsViewSet, basename="customer-fligths")


urlpatterns = (
    router.urls
    + customers_router.urls
    + titles_router.urls
    # + sub_collection_router.urls
    # + shop_router.urls
)
# ) + [path('itemsinshop/<str:cart_id>/', views.get_product_in_shop)]


# router.register("customers", views.CustomersViewSet, basename='customers')


# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
