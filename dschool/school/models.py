from django.db import models

class FAQS(models.Model):
    question = models.CharField('Вопрос', max_length=100, null=False) 
    answer = models.CharField('Ответ', max_length=300, null=False)


    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Ответы'

class Cards(models.Model):
    id = models.CharField('ID', max_length=2, null=False, primary_key=True)
    title = models.CharField('Название', max_length=30, null=False) 
    pagelink = models.CharField('Ссылка на категорию', max_length=30, null=False)
    imglink = models.URLField('Изображение', null=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Земной транспорт'
        verbose_name_plural = 'Транспорт'

class Extreme(models.Model):
    id = models.CharField('ID', max_length=2, null=False, primary_key=True)
    title = models.CharField('Название', max_length=30, null=False) 
    pagelink = models.CharField('Ссылка на категорию', max_length=30, null=False)
    imglink = models.URLField('Изображение', null=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экстрим'
        verbose_name_plural = 'Экстримальное вождение'

