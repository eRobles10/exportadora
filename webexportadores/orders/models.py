from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.


class OrderStatus(models.Model):
    name = models.CharField(max_length=200, verbose_name="Status")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")
    active = models.BooleanField(verbose_name="Active", blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product")
    status = models.BooleanField(verbose_name="Active", blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created"]  # ordernacion de mas reciente a mas viejo

    def __str__(self):
        return self.name


class Border(models.Model):
    name = models.CharField(max_length=200, verbose_name="Border")
    description = models.TextField(max_length=600, verbose_name="Description")
    status = models.BooleanField(verbose_name="Active", blank=True, null=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Border"
        verbose_name_plural = "Borders"
        ordering = ["-created"]  # ordernacion de mas reciente a mas viejo

    def __str__(self):
        return self.name


class Order(models.Model):
    author = models.ForeignKey(
        User, verbose_name="Autor", on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(
        verbose_name="Quantity", validators=[MinValueValidator(25)])
    product = models.ForeignKey(
        Products, verbose_name="Product", related_name="get_products", on_delete=models.PROTECT)
    border = models.ForeignKey(
        Border, verbose_name="Border", related_name="get_border", on_delete=models.PROTECT)
    orderStatus = models.ForeignKey(
        OrderStatus, verbose_name="Order Status", related_name="get_order_status", on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")

    def __str__(self):
        return str(self.id)
