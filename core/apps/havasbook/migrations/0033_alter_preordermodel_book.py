# Generated by Django 5.1.3 on 2025-04-15 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0032_preordermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preordermodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='havasbook.bookmodel'),
        ),
    ]
