# Generated by Django 5.1.3 on 2025-04-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0040_alter_cartitemmodel_color_alter_cartitemmodel_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemmodel',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cartitemmodel',
            name='size',
        ),
    ]
