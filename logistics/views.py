from rest_framework import viewsets
from django.shortcuts import render
from .models import (
    Package,
    Order,
    Payment,
    Notification,
    ShippingRate,
    CustomerService,
    Coupon,
    Membership,
    Report,
    WarehouseEntry,
    WarehouseExit,
)
from .serializers import (
    PackageSerializer,
    OrderSerializer,
    PaymentSerializer,
    NotificationSerializer,
    ShippingRateSerializer,
    CustomerServiceSerializer,
    CouponSerializer,
    MembershipSerializer,
    ReportSerializer,
    WarehouseEntrySerializer,
    WarehouseExitSerializer,
)


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class ShippingRateViewSet(viewsets.ModelViewSet):
    queryset = ShippingRate.objects.all()
    serializer_class = ShippingRateSerializer


class CustomerServiceViewSet(viewsets.ModelViewSet):
    queryset = CustomerService.objects.all()
    serializer_class = CustomerServiceSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class WarehouseEntryViewSet(viewsets.ModelViewSet):
    queryset = WarehouseEntry.objects.all()
    serializer_class = WarehouseEntrySerializer


class WarehouseExitViewSet(viewsets.ModelViewSet):
    queryset = WarehouseExit.objects.all()
    serializer_class = WarehouseExitSerializer


# 网页视图
def home(request):
    return render(request, "logistics/home.html")


def package_list(request):
    packages = Package.objects.all()
    return render(request, "logistics/packages.html", {"packages": packages})


def order_list(request):
    orders = Order.objects.all()
    return render(request, "logistics/orders.html", {"orders": orders})
