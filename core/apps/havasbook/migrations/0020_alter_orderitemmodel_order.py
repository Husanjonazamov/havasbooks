# Generated by Django 5.1.3 on 2025-04-10 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0019_alter_locationmodel_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='havasbook.ordermodel'),
        ),
    ]
