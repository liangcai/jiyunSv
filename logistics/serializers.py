from rest_framework import serializers
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


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class ShippingRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRate
        fields = "__all__"


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class WarehouseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseEntry
        fields = "__all__"


class WarehouseExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseExit
        fields = "__all__"
