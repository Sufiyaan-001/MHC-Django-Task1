# Generated by Django 5.1.4 on 2025-01-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groceries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groces',
            name='Quantity',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
