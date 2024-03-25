from rest_framework_nested import routers
from . import views  # CustomersViewSet, OrdersViewSet, OrderItemsViewSet

router = routers.DefaultRouter()

router.register("countries", views.CountryViewSet, basename="countries")
router.register("idtypes", views.IdTypeViewSet, basename="idtypes")

router.register("levels", views.LevelViewSet, basename="levels")
router.register("areas", views.AreaViewSet, basename="areas")
router.register("posts", views.PostViewSet, basename="posts")
router.register("laws", views.LawsViewSet, basename="laws")

router.register("postview", views.PostViewViewSet, basename="postview")
router.register("sections", views.SectionViewSet, basename="sections")
router.register("gallerys", views.GalleryViewSet, basename="gallerys")

router.register("doctors", views.DoctorViewSet, basename="doctors")
router.register("messages", views.MessagesViewSet, basename="messages")
router.register("postimage", views.PostImagesViewSet, basename="postimages")
router.register("teams", views.TeamViewSet, basename="team")


doctors_router = routers.NestedSimpleRouter(
    router, r"doctors", lookup="doctor")
doctors_router.register(
    r"doctorimages", views.DoctorImageViewSet, basename="doctor-doctorimages"
)
doctors_router.register(
    r"doctorids", views.DoctorIDViewSet, basename="doctor-doctorids"
)

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(
    r"postimages", views.PostImagesViewSet, basename="post-postimages"
)

gallerys_router = routers.NestedSimpleRouter(
    router, r"gallerys", lookup="gallery")
gallerys_router.register(r"images", views.ImagesGalleryViewSet,
                         basename="gallery-images")

# router.register("shops", views.ShopViewSet, basename="shops")
# router.register("orders", views.OrdersViewSet, basename="orders")
# router.register("delivers", views.DeliverViewSet, basename="delivers")
# router.register("products", views.ProductsViewSet, basename="products")
# router.register("customers", views.CustomerViewSet, basename="customers")
# router.register("customeraddress", views.CustomerAddressViewSet,
#                 basename="customeraddress")
# router.register("customerpayments", views.CustomerPaymentViewSet,
#                 basename="customerpayments")
# router.register("shopmanage", views.ShopManageViewSet, basename="shopmanage")
# router.register("collections", views.CollectionViewSet, basename="collections")
# router.register("productsinshops", views.ProductsInShopsViewSet,
#                 basename="productsinshops")
# router.register("deliverorders", views.DeliverOrderViewSet,
#                 basename="deliverorders")


# router.register("orderfordeliver", views.OrderForDeliverViewSet,
#                 basename="orderfordeliver")


# router.register("productshop", views.ProductsInShopsBySlugViewSet,
#                 basename="productshop")

# router.register("shopmanagebyslug", views.ShopManageBySlugViewSet,
#                 basename="shopmanagebyslug")


# router.register("shopsbyslug", views.ShopsBySlugViewSet,
#                 basename="shopsbyslug")


# # orders_router = routers.NestedSimpleRouter(router, 'orders', lookup='order')
# # orders_router.register(
# #     'orderitems', views.OrderItemsViewSet, basename='order-orderitems')


# customers_router = routers.NestedSimpleRouter(
#     router, r"customers", lookup="customer")
# customers_router.register(r"addresses", views.CustomerAddressViewSet,
#                           basename="customer-addresses")

# orders_router = routers.NestedSimpleRouter(router, r"orders", lookup="order")
# orders_router.register(
#     r"orderitems", views.OrderItemsViewSet, basename="order-orderitems"
# )

# # orders_router.register(
# #     r"delivers", views.DeliverOrderViewSet, basename="order-delivers"
# # )

# carts_router = routers.NestedSimpleRouter(router, r"carts", lookup="cart")
# carts_router.register(r"cartitems", views.CartItemsViewSet,
#                       basename="cart-cartitems")

# shopmanages_router = routers.NestedSimpleRouter(
#     router, r"shopmanage", lookup="shop")

# shopmanages_router.register(
#     r"shopmanageproducts",
#     views.ShopManageProductViewSet,
#     basename="shop-shopmanageproducts",
# )


# shops_router = routers.NestedSimpleRouter(router, r"shops", lookup="shop")
# shops_router.register(r"products", views.ShopProductViewSet,
#                       basename="shop-products")


# delivers_router = routers.NestedSimpleRouter(
#     router, r"delivers", lookup="deliver")
# delivers_router.register(r"postcodes", views.DeliverPostViewSet,
#                          basename="deliver-postcodes")


urlpatterns = (
    router.urls
    + posts_router.urls
    + gallerys_router.urls
    + doctors_router.urls
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
