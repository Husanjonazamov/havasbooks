# Generated by Django 5.1.3 on 2025-04-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0023_alter_orderitemmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Telefon raqam'),
        ),
    ]
