# Generated by Django 5.1.3 on 2025-04-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0013_ordermodel_locationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name'),
        ),
    ]
