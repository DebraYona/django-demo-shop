from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=50, verbose_name="name"
    )

    class Meta:
        ordering = ['name']
        verbose_name = ("category")

    def __str__(self):
        return self.name

    @property
    def action_list(self):
        return ('change', 'delete')