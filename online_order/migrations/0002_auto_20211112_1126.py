# Generated by Django 3.2.9 on 2021-11-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivary',
            field=models.CharField(blank=True, choices=[('Out of delivary', 'Out of delivary'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
