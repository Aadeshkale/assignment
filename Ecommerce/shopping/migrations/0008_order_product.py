# Generated by Django 3.1.1 on 2020-10-14 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0007_auto_20201011_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('house_no', models.CharField(blank=True, max_length=100, null=True)),
                ('area_name', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('mob1', models.CharField(max_length=100, null=True)),
                ('mob2', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('landmark', models.CharField(max_length=100, null=True)),
                ('pro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]