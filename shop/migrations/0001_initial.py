# Generated by Django 3.1.3 on 2020-11-30 21:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=40)),
                ('creation_date', models.DateField(blank=True, default=datetime.date.today)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('legal_creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('target_total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=40)),
                ('order_status', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='abv')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.product')),
            ],
        ),
    ]
