# Generated by Django 4.2.5 on 2023-10-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]