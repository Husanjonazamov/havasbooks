# Generated by Django 5.1.3 on 2025-04-08 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0015_remove_ordermodel_name_ordermodel_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name="Ko'rilganlar soni"),
        ),
        migrations.AlterField(
            model_name='bookimagemodel',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='havasbook.bookmodel', verbose_name='Kitob'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Asl narxi'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Chegirmadagi narxi'),
        ),
    ]
