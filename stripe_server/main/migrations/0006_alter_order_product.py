# Generated by Django 4.1.3 on 2022-11-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='main.item'),
        ),
    ]
