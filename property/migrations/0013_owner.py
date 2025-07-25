# Generated by Django 5.2.4 on 2025-07-10 11:48

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20250710_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(blank=True, related_name='owners', to='property.flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
