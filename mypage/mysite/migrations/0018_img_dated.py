# Generated by Django 3.0.3 on 2020-04-15 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20200415_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='dated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
