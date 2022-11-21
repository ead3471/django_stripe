from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Currency(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    code = models.CharField(max_length=3, verbose_name='Код валюты')

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование',
                            blank=False,
                            null=False
                            )
    description = models.TextField(verbose_name='Описание',
                                   blank=False,
                                   null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Пользователь')
    product = models.ManyToManyField('Item', related_name='products',)
    created = models.DateTimeField(auto_now_add=True)
