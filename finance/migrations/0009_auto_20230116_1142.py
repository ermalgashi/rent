# Generated by Django 3.2.16 on 2023-01-16 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("finance", "0008_reservation_fuel_capacity"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="payment",
            field=models.CharField(
                choices=[("Cash", "Kesh"), ("Card", "Kartelë")],
                default="Cash",
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Expenses",
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
                (
                    "expense_type",
                    models.CharField(
                        choices=[
                            ("Terheqje", "TERHEQJE"),
                            ("Servis", "SERVIS"),
                            ("Reprezentacion", "REPREZENTACION"),
                            ("Tjeter", "TJETER"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
