# Generated by Django 4.1.3 on 2022-11-20 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.currency'),
            preserve_default=False,
        ),
    ]
