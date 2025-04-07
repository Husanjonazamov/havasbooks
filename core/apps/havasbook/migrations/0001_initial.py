# Generated by Django 5.1.3 on 2025-04-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('name_kril', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='banner-image/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'BannerModel',
                'verbose_name_plural': 'BannerModels',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'BookModel',
                'verbose_name_plural': 'BookModels',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'CategoryModel',
                'verbose_name_plural': 'CategoryModels',
                'db_table': 'category',
            },
        ),
    ]
