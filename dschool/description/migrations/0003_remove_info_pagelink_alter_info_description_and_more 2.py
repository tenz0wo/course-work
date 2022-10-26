# Generated by Django 4.0.4 on 2022-09-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('description', '0002_alter_info_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='pagelink',
        ),
        migrations.AlterField(
            model_name='info',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='info',
            name='description_high',
            field=models.CharField(max_length=300, null=True, verbose_name='Описание максимальной'),
        ),
        migrations.AlterField(
            model_name='info',
            name='description_mid',
            field=models.CharField(max_length=300, null=True, verbose_name='Описание средней'),
        ),
        migrations.AlterField(
            model_name='info',
            name='description_min',
            field=models.CharField(max_length=300, null=True, verbose_name='Описание минимальной'),
        ),
        migrations.AlterField(
            model_name='info',
            name='price_high',
            field=models.CharField(max_length=10, null=True, verbose_name='Максимальная цена'),
        ),
        migrations.AlterField(
            model_name='info',
            name='price_mid',
            field=models.CharField(max_length=10, null=True, verbose_name='Средняя цена'),
        ),
        migrations.AlterField(
            model_name='info',
            name='price_min',
            field=models.CharField(max_length=10, null=True, verbose_name='Минимальная цена'),
        ),
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(max_length=30, null=True, verbose_name='Название'),
        ),
    ]