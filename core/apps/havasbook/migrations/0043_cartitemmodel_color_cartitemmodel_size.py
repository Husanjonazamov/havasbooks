# Generated by Django 5.1.3 on 2025-04-17 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0042_bookmodel_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemmodel',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='havasbook.colormodel'),
        ),
        migrations.AddField(
            model_name='cartitemmodel',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='havasbook.sizemodel'),
        ),
    ]
