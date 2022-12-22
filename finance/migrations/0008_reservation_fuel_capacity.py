# Generated by Django 3.2.16 on 2022-12-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_remove_reservation_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='fuel_capacity',
            field=models.CharField(choices=[('1/4', '1/4'), ('2/4', '2/4'), ('3/4', '3/4'), ('4/4', '4/4')], default='1/4', max_length=10),
            preserve_default=False,
        ),
    ]