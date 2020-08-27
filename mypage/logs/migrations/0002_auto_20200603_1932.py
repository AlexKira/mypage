# Generated by Django 3.0.3 on 2020-06-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]