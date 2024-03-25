from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet
from django.urls import path
router = routers.DefaultRouter()





# manage cart
# router.register("customers", views.CartViewSet, basename="customers")
router.register("cities", views.CityViewSet, basename="cities")
router.register("countries", views.CountryViewSet, basename="countries")
router.register("streets", views.StreetViewSet, basename="streets")

router.register("houses", views.HouseViewSet, basename="countries")




urlpatterns = (
    router.urls
  
)