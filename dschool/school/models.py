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

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


CATEGORY_CHOICES = [
    ('Категория B', 'Категория B'),
    ('Категория A', 'Категория A'),
    ('Категория BE', 'Категория BE'),
    ('Категория A1', 'Категория A1'),
    ('Категория C', 'Категория C'),
    ('Подкатегория C1', 'Подкатегория C1'),
    ('Экстремальное вождение', 'Экстремальное вождение'),
    ('Ралли', 'Ралли'),
    ('Дрифт', 'Дрифт'),
    ('Специализированные программы', 'Специализированные программы'),
    
]   

GROUP_CHOICES = {
    ('Группа 1', 'Начало обучения 07.01.2023'),
    ('Группа 2', 'Начало обучения 15.04.2023'),
    ('Группа 3', 'Начало обучения 30.06.2023'),
}

ADDRESS_CHOICES = {
    ('Москва', 'Большая Тульская ул., 2, 8 офис; 2 этаж, Москва, 115191'),
    ('Москва', 'улица Казакова д6 стр1, Москва, 105064'),
    ('Москва', 'Петровка ул., 15с1, Москва, 107031'),
}

class Ticket(models.Model):
    first_name = models.CharField('Имя', max_length=100, null=False) 
    last_name = models.CharField('Фамилия', max_length=100, null=False) 
    mail = models.CharField('Почта', max_length=150, null=False)
    address = models.CharField('Адрес', max_length=200, null=False) 
    address_autoschool = models.CharField('Адрес автошколы', max_length=200, null=False, choices=ADDRESS_CHOICES)     
    category = models.CharField("Категория", max_length=100, null=False, choices=CATEGORY_CHOICES) 
    group = models.CharField("Группа", max_length=100, null=False, choices=GROUP_CHOICES) 


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Форма' 
