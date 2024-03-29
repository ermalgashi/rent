# Generated by Django 3.2.16 on 2022-11-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_make", models.CharField(max_length=20)),
                ("car_model", models.CharField(max_length=20)),
                ("car_year", models.CharField(max_length=10)),
                ("car_engine", models.CharField(max_length=10)),
                ("car_fuel_type", models.CharField(max_length=10)),
                ("car_capacity", models.IntegerField()),
                ("registration_number", models.CharField(max_length=20)),
                ("registration_date", models.DateField()),
                ("registration_expiration_date", models.DateField()),
                ("vin", models.CharField(max_length=30)),
                ("color", models.CharField(max_length=20)),
                ("owner", models.CharField(max_length=20)),
            ],
        ),
    ]
