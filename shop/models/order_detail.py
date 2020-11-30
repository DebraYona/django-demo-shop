from datetime import datetime,date

from django.db import models

from core.models import Product
from shop.models.order import Order


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_index=True, related_name="detail"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_index=True, related_name="product"
    )
    quantity = models.IntegerField()
    unit_price_amount = models.DecimalField(
        max_digits=6, decimal_places=2
    )
    total_amount = models.DecimalField(
        blank=True, null=True, max_digits=6, decimal_places=2,
        verbose_name="abv"
    )

    def __str__(self):
        return self.order.order_code