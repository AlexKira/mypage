# Generated by Django 3.0.3 on 2020-04-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Наименование услуги', 'verbose_name_plural': 'Вкладка: УСЛУГИ'},
        ),
        migrations.AlterField(
            model_name='service',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(verbose_name='Содержание услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование услуги'),
        ),
    ]
