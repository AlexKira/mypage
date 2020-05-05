# Generated by Django 3.0.3 on 2020-04-11 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200410_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mysite.Service', verbose_name='Редактирование услуги')),
            ],
            options={
                'verbose_name_plural': 'Редактирование услуги',
            },
        ),
    ]
