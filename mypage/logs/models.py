from django.db import models
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Aвтop' )
    body = models.TextField(verbose_name='Coдepжaниe')
    email = models.EmailField()
    active = models.BooleanField(default=True, db_index = True, verbose_name = 'Выводить на экран?')
    date_added = models.DateTimeField(auto_now_add=True,db_index = True, verbose_name='Опубликован')


    class Meta:
        verbose_name_plural = 'Меню вкладки: ОТЗЫВЫ'
        verbose_name = 'ОТЗЫВЫ'
        ordering = [ 'date_added' ]

    def __str__(self):
        return self.name
