# Generated by Django 5.1.3 on 2025-04-08 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0016_bookmodel_views_alter_bookimagemodel_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitemmodel',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='havasbook.cartmodel'),
        ),
    ]
