# Generated by Django 4.1.7 on 2023-05-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablebooking', '0008_remove_tablebooking_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='booking_phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
