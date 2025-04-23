from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet

router = routers.DefaultRouter()

router.register("customers", views.CustomerViewSet, basename="customers")

router.register("clients", views.ClientsViewSet, basename="clients")
router.register("products", views.ProductsViewSet, basename="products")
router.register("destines", views.DestinesViewSet, basename="destines")
router.register("sells", views.SellsAllViewSet, basename="sells")
router.register("expenses", views.ExpensesViewSet, basename="expenses")
router.register("payments", views.PaymentsAllViewSet, basename="payments")
router.register("balances", views.SellsPaymentsExpensesViewSet, basename="balance")


clients_router = routers.NestedSimpleRouter(router, r"clients", lookup="client")

clients_router.register(r"sells", views.SellsByClientViewSet, basename="client-sells")
clients_router.register(r"payments", views.PaymentsByClientViewSet, basename="client-payments")

destines_router = routers.NestedSimpleRouter(router, r"destines", lookup="destine")
destines_router.register(r"expenses", views.ExpensesViewSet, basename="destine-expenses")
destines_router.register(r"payments", views.ExpensePaymentsViewSet, basename="destine-payments")


urlpatterns = (router.urls+ clients_router.urls+destines_router.urls)


# /domain/ <- Domains list
# /domain/{pk}/ <- One domain, from {pk}
# /domain/{domain_pk}/nameservers/ <- Nameservers of domain from {domain_pk}
# /domain/{domain_pk}/nameservers/{pk} <- Specific nameserver from {pk}, of domain from {domain_pk}
