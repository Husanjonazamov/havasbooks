# Generated by Django 5.1.3 on 2025-04-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havasbook', '0046_preordermodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preordermodel',
            name='status',
            field=models.CharField(choices=[('new', 'Yangi'), ('accepted', 'Qabul qilindi'), ('cancelled', 'Bekor qilindi')], default='new', max_length=20, verbose_name='Status'),
        ),
    ]
