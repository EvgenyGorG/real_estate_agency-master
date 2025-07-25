# Generated by Django 5.2.4 on 2025-07-10 08:11

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_flat_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
