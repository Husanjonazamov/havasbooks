# Generated by Django 5.1.3 on 2025-04-08 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0010_categorymodel_image_categorymodel_name_kril_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='havasbook.categorymodel', verbose_name='Kategoriylar'),
        ),
    ]
