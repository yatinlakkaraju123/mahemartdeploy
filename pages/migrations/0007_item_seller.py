# Generated by Django 4.1.1 on 2022-11-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_order_checkout_address_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.CharField(max_length=50, null=True),
        ),
    ]