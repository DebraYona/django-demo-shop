from datetime import datetime,date

from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    CONDITION1 = 1
    CONDITION2 = 2
    CONDITION3 = 3
    CONDITIONS_CHOICES = [
        (CONDITION1, 'Pago en 15 dias'),
        (CONDITION2, 'Pago en 30 dias'),
        (CONDITION3, 'Pago inmediato'),
    ]
    order_code = models.CharField(
        max_length=40
    )
    creation_date = models.DateField(default=date.today, blank=True )
    delivery_date = models.DateField(blank=True, null=True,)
    legal_creation_date = models.DateTimeField(default=datetime.now, blank=True)
    total_amount = models.DecimalField(
        max_digits=6, decimal_places=2
    )
    target_total_amount = models.DecimalField(
        max_digits=8, decimal_places=2
    )
    address = models.CharField(
        max_length=40
    )
    order_status = models.IntegerField()
    client = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, db_index=True,
        related_name="client"
    )