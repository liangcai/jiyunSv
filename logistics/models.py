from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    tracking_number = models.CharField(max_length=100)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    arrival_date = models.DateTimeField()
    photos = models.ImageField(upload_to="package_photos/", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse_location = models.CharField(max_length=100)

    def __str__(self):
        return self.tracking_number


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    packages = models.ManyToManyField(Package)
    shipping_method = models.CharField(max_length=50)
    total_cost = models.FloatField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.order.order_number} - {self.amount}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"


class ShippingRate(models.Model):
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return f"Rate for {self.destination}"


class CustomerService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Query from {self.user.username}"


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.FloatField()
    expiry_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.code


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)
    points = models.IntegerField()
    benefits = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.level}"


class Report(models.Model):
    report_type = models.CharField(max_length=100)
    data = models.JSONField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_type


class WarehouseEntry(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    photos = models.ImageField(upload_to="entry_photos/", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    warehouse_location = models.CharField(max_length=100)

    def __str__(self):
        return f"Entry for {self.package.tracking_number}"


class WarehouseExit(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    exit_date = models.DateTimeField(auto_now_add=True)
    packages = models.ManyToManyField(Package)
    shipping_method = models.CharField(max_length=50)
    total_weight = models.FloatField()
    total_dimensions = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Exit for order {self.order.order_number}"
