# Generated by Django 5.1.4 on 2025-01-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cloths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Type', models.CharField(max_length=255)),
                ('Shipping_agent', models.CharField(max_length=255)),
                ('Size', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]