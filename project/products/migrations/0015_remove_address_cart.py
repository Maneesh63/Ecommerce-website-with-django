# Generated by Django 4.2.6 on 2024-06-19 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_address_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='cart',
        ),
    ]
