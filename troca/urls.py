from rest_framework_nested import routers
from . import views  

router = routers.DefaultRouter()


router.register("friends", views.FriendViewSet, basename="friends")
router.register("customers", views.CustomerViewSet,
                basename="customers")
router.register("transactions", views.TransactionViewSet,
                basename="transactions")

router.register("charges", views.ChargeViewSet, basename="charges")


urlpatterns = router.urls
