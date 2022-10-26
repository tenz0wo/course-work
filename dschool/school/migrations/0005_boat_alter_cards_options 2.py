# Generated by Django 4.0.4 on 2022-09-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('pagelink', models.CharField(max_length=15, verbose_name='Ссылка на категорию')),
                ('imglink', models.URLField(verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Водный транспорт',
                'verbose_name_plural': 'Транспорт',
            },
        ),
        migrations.AlterModelOptions(
            name='cards',
            options={'verbose_name': 'Земной транспорт', 'verbose_name_plural': 'Транспорт'},
        ),
    ]
