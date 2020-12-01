from datetime import datetime,date

from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    STATE1 = 1
    STATE2 = 2
    STATE3 = 3
    STATES_CHOICES = [
        (STATE1, 'carrito'),
        (STATE2, 'pagado'),
        (STATE3, 'entregado'),
    ]
    order_code = models.CharField(
        max_length=40
    )
    creation_date = models.DateField(default=date.today, blank=True )

    legal_creation_date = models.DateTimeField(default=datetime.now, blank=True)
    total_amount = models.DecimalField(
        max_digits=6, decimal_places=2
    )


    order_status = models.CharField(
        choices=STATES_CHOICES,
        max_length=40
    )
    client = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, db_index=True,
        related_name="client"
    )

    def __str__(self):
        return self.order_code
