# Generated by Django 3.0.3 on 2020-04-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0019_auto_20200415_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='dated',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]