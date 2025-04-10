# Generated by Django 5.1.3 on 2025-04-08 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0011_bookmodel_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Foydalanuvchi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CartModel',
                'verbose_name_plural': 'CartModels',
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='CartitemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveBigIntegerField(default=1, verbose_name='Mahsulot soni')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='havasbook.bookmodel')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='havasbook.cartmodel')),
            ],
            options={
                'verbose_name': 'CartitemModel',
                'verbose_name_plural': 'CartitemModels',
                'db_table': 'cartItem',
            },
        ),
    ]
