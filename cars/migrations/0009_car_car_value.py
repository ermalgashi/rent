# Generated by Django 3.2.16 on 2023-02-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0008_alter_car_insurance_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="car_value",
            field=models.IntegerField(default=17000),
            preserve_default=False,
        ),
    ]
