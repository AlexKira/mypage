# Generated by Django 3.0.3 on 2020-04-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0008_auto_20200428_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newswork',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='image.NewsWork'),
        ),
    ]
