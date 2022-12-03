# Generated by Django 4.1.3 on 2022-11-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=20)),
                ("surname", models.CharField(max_length=20)),
                ("license_id", models.CharField(max_length=50)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("ALBANIA", "Albania"),
                            ("KOSOVO", "Kosovo"),
                            ("ITALY", "Italy"),
                            ("USA", "Usa"),
                        ],
                        default="ITALY",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
