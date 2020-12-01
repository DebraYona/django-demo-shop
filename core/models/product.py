from django.db import models


class Product(models.Model):
    category = models.ForeignKey(
        'core.Category', verbose_name="category", on_delete=models.CASCADE,
        db_index=True, related_name="product", blank=True, null=True,
    )
    brand = models.CharField(
        max_length=150,
        verbose_name="brand"
    )
    name = models.CharField(
        max_length=150, verbose_name="name"
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="description"
    )
    image = models.ImageField(
        blank=True, null=True, upload_to='inventory/products/images/',
        verbose_name="image"
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.0
    )

    class Meta:
        ordering = ['name']
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name