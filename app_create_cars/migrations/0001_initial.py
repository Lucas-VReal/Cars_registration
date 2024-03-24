# Generated by Django 5.0.3 on 2024-03-24 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.TextField(max_length=255)),
                ('car_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
    ]
