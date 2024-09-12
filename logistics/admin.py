from django.contrib import admin
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


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "tracking_number",
        "weight",
        "dimensions",
        "status",
        "arrival_date",
        "user",
    )
    search_fields = ("tracking_number", "user__username")
    list_filter = ("status", "arrival_date")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "user",
        "shipping_method",
        "total_cost",
        "status",
        "created_at",
    )
    search_fields = ("order_number", "user__username")
    list_filter = ("status", "created_at")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "payment_method", "payment_date", "status")
    search_fields = ("order__order_number",)
    list_filter = ("status", "payment_date")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created_at", "is_read")
    search_fields = ("user__username", "message")
    list_filter = ("is_read", "created_at")


@admin.register(ShippingRate)
class ShippingRateAdmin(admin.ModelAdmin):
    list_display = ("weight", "dimensions", "destination", "rate")
    search_fields = ("destination",)
    list_filter = ("destination",)


@admin.register(CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):
    list_display = ("user", "query", "response", "created_at", "status")
    search_fields = ("user__username", "query")
    list_filter = ("status", "created_at")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount", "expiry_date", "user")
    search_fields = ("code", "user__username")
    list_filter = ("expiry_date",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "level", "points", "benefits")
    search_fields = ("user__username", "level")
    list_filter = ("level",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("report_type", "generated_at")
    search_fields = ("report_type",)
    list_filter = ("generated_at",)


@admin.register(WarehouseEntry)
class WarehouseEntryAdmin(admin.ModelAdmin):
    list_display = (
        "package",
        "entry_date",
        "weight",
        "dimensions",
        "warehouse_location",
    )
    search_fields = ("package__tracking_number",)
    list_filter = ("entry_date",)


@admin.register(WarehouseExit)
class WarehouseExitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "exit_date",
        "shipping_method",
        "total_weight",
        "total_dimensions",
    )
    search_fields = ("order__order_number",)
    list_filter = ("exit_date",)
