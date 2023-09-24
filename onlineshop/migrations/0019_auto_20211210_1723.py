# Generated by Django 3.2.9 on 2021-12-10 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0018_auto_20211209_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 959647)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_join',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 956655)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 956655)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 962639), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 17, 17, 23, 16, 962639)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 962639), null=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 963686)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 961642)),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 17, 23, 16, 966666)),
        ),
    ]