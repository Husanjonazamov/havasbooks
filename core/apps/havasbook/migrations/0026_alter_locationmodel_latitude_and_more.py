# Generated by Django 5.1.3 on 2025-04-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0025_alter_ordermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='latitude',
            field=models.CharField(max_length=100, verbose_name='Kenglik'),
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='longitude',
            field=models.CharField(max_length=100, verbose_name='Uzunlik'),
        ),
    ]
