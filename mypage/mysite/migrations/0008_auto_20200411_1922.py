# Generated by Django 3.0.3 on 2020-04-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200411_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Содержание услуги', 'verbose_name_plural': 'Содержание услуги'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Наименование услуги', 'verbose_name_plural': 'Наименование услуги'},
        ),
    ]
