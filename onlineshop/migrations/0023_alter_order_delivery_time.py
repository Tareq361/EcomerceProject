# Generated by Django 3.2.9 on 2021-12-30 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0022_alter_order_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 14, 6, 58, 98619, tzinfo=utc)),
        ),
    ]
