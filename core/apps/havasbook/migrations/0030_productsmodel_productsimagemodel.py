# Generated by Django 5.1.3 on 2025-04-14 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0029_bookmodel_is_preorder_bookmodel_sold_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mahsulot tavsifi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-image/', verbose_name='Rasm')),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Asl narxi')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Chegirmadagi narxi')),
                ('is_discount', models.BooleanField(default=False, verbose_name='Chegirma bormi ?')),
                ('discount_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='chegirma foizi')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Kitob soni')),
                ('sold_count', models.PositiveIntegerField(default=0, verbose_name='Sotilganlar soni')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")),
                ('is_preorder', models.BooleanField(default=False, verbose_name='Oldindan buyurtma bormi?')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='havasbook.categorymodel', verbose_name='Kategoriylar')),
            ],
            options={
                'verbose_name': 'ProductsModel',
                'verbose_name_plural': 'ProductsModels',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductsimageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product-image/', verbose_name='Rasm')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='havasbook.productsmodel', verbose_name='Kitob')),
            ],
            options={
                'verbose_name': 'ProductsimageModel',
                'verbose_name_plural': 'ProductsimageModels',
                'db_table': 'productsImage',
            },
        ),
    ]
