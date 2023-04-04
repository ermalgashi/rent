# Generated by Django 3.2.16 on 2022-11-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_rename_cars_car"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="insurance_type",
            field=models.CharField(
                choices=[
                    ("CASCO", "Casco"),
                    ("BASIC", "Basic"),
                    ("REGIONAL", "Regional"),
                    ("INTERNATIONAL", "International"),
                ],
                default="DIESEL",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_fuel_type",
            field=models.CharField(
                choices=[
                    ("DIESEL", "Diesel"),
                    ("PETROL", "Petrol"),
                    ("ELECTRIC", "Electric"),
                    ("PROPANE", "Propane"),
                ],
                default="DIESEL",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="registration_number",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="vin",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
