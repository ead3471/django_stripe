# Generated by Django 4.1.3 on 2022-11-21 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_discount_tax_order_discount_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordders', to='main.tax', verbose_name='Налог, %'),
        ),
    ]
