# Generated by Django 5.2.4 on 2025-07-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Новостройка'),
        ),
    ]
