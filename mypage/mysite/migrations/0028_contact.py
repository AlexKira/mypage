# Generated by Django 3.0.3 on 2020-07-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0027_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=500, verbose_name='Имя')),
                ('email', models.CharField(max_length=500, verbose_name='Почта')),
                ('text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Дополнительное поле')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Меню вкладки: КОНТАКТЫ',
            },
        ),
    ]
