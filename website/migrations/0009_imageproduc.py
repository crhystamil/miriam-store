# Generated by Django 5.0 on 2023-12-21 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_brand_sufix'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.product')),
            ],
        ),
    ]