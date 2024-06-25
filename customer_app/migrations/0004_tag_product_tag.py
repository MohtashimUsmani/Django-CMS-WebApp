# Generated by Django 5.1a1 on 2024-06-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0003_order_customer_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='customer_app.tag'),
        ),
    ]