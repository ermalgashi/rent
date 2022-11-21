# Generated by Django 4.1.3 on 2022-11-21 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_insurance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
