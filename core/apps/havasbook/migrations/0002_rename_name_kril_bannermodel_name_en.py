# Generated by Django 5.1.3 on 2025-04-07 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannermodel',
            old_name='name_kril',
            new_name='name_en',
        ),
    ]
