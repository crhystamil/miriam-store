# Generated by Django 5.0 on 2023-12-30 22:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_remove_inventory_month_remove_product_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sales',
            name='month',
        ),
        migrations.AddField(
            model_name='sales',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='sales',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='website.seller'),
        ),
    ]
