from django.db import models

class Info(models.Model):
    id = models.CharField('ID', max_length=2, null=False, primary_key=True)
    title = models.CharField('Название', max_length=30, null=True) 
    description = models.CharField('Описание', max_length=200, null=True)
    price_min = models.CharField('Минимальная цена', max_length=10, null=True)
    price_mid = models.CharField('Средняя цена', max_length=10, null=True)
    price_high = models.CharField('Максимальная цена', max_length=10, null=True)
    description_min = models.CharField('Описание минимальной', max_length=300, null=True)
    description_mid = models.CharField('Описание средней', max_length=300, null=True)
    description_high = models.CharField('Описание максимальной', max_length=300, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация о категориях'