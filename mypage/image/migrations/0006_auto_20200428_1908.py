# Generated by Django 3.0.3 on 2020-04-28 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_auto_20200428_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newswork',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='image.NewsWork'),
            preserve_default=False,
        ),
    ]