from django.db import models


class Product(models.Model):
    categories = models.ManyToManyField(
        'core.Category', verbose_name="categories"
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

    class Meta:
        ordering = ['name']
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name