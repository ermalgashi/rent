# Generated by Django 4.1.3 on 2022-11-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0003_alter_reservation_pickup_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="pickup_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="return_date",
            field=models.DateTimeField(),
        ),
    ]
