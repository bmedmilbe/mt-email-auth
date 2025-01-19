from rest_framework_nested import routers
from . import views  

router = routers.DefaultRouter()


router.register("friends", views.FriendViewSet, basename="friends")
friend_urls = routers.NestedDefaultRouter(router,r'friends', lookup='friend')
friend_urls.register(r'payments', views.FriendPaymentViewSet, basename='friend-payments')
router.register("customers", views.CustomerViewSet,
                basename="customers")
router.register("transactions", views.TransactionViewSet,
                basename="transactions")

router.register("charges", views.ChargeViewSet, basename="charges")


urlpatterns = router.urls + friend_urls.urls
