# Generated by Django 5.1a1 on 2024-06-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
