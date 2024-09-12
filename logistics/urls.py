from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PackageViewSet,
    OrderViewSet,
    PaymentViewSet,
    NotificationViewSet,
    ShippingRateViewSet,
    CustomerServiceViewSet,
    CouponViewSet,
    MembershipViewSet,
    ReportViewSet,
    WarehouseEntryViewSet,
    WarehouseExitViewSet,
    home,
    package_list,
    order_list,
)

router = DefaultRouter()
router.register(r"packages", PackageViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"notifications", NotificationViewSet)
router.register(r"shipping-rates", ShippingRateViewSet)
router.register(r"customer-services", CustomerServiceViewSet)
router.register(r"coupons", CouponViewSet)
router.register(r"memberships", MembershipViewSet)
router.register(r"reports", ReportViewSet)
router.register(r"warehouse-entries", WarehouseEntryViewSet)
router.register(r"warehouse-exits", WarehouseExitViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("packages/", package_list, name="packages"),
    path("orders/", order_list, name="orders"),
    path("api/", include(router.urls)),
]
