# Generated by Django 3.1.1 on 2021-07-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20210628_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Video upload'),
        ),
    ]
