# Generated by Django 5.0 on 2024-01-04 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_inventory_price_seller_sale_profit_sale_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product',
            new_name='product_inv',
        ),
    ]
