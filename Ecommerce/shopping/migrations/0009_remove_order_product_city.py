# Generated by Django 3.1.1 on 2020-10-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_product',
            name='city',
        ),
    ]