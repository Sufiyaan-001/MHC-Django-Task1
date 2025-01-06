# Generated by Django 5.1.4 on 2025-01-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Type', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=255)),
                ('Rating', models.FloatField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
