# Generated by Django 5.1 on 2024-09-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0009_customer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.TextField(default='', max_length=100),
        ),
    ]
