# Generated by Django 3.1.1 on 2021-06-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210628_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='about',
            name='content_es',
            field=models.TextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_es',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
    ]
