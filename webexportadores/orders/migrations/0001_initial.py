# Generated by Django 3.1.1 on 2021-06-23 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Frontiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Frontier')),
                ('description', models.TextField(max_length=600, verbose_name='Description')),
                ('status', models.BooleanField(blank=True, null=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('active', models.BooleanField(blank=True, null=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product')),
                ('status', models.BooleanField(blank=True, null=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('frontier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_frontiers', to='orders.frontiers', verbose_name='Frontier')),
                ('orderStatus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_frontiers', to='orders.orderstatus', verbose_name='Frontier')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_products', to='orders.products', verbose_name='Product')),
            ],
        ),
    ]