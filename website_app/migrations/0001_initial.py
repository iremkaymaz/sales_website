# Generated by Django 5.1 on 2024-10-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('telephone', models.CharField(default='', max_length=11)),
                ('province', models.CharField(default='', max_length=20)),
                ('district', models.CharField(default='', max_length=30)),
                ('address', models.TextField(default='', max_length=200)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('size', models.TextField(default='', max_length=10)),
                ('colour', models.CharField(default='', max_length=30)),
                ('payment_method', models.TextField(default='', max_length=70)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(default='', max_length=100)),
            ],
        ),
    ]
