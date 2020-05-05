from django.db import models

# Create your models here.
'''______Вкладка "УСЛУГИ"______'''

class Service(models.Model):
	title = models.CharField(max_length=200, verbose_name= 'Наименование услуги')
	text = models.TextField(verbose_name= 'Содержание услуги')
	date_added = models.DateTimeField(auto_now_add=True, verbose_name= 'Дата')


	class Meta:
		verbose_name_plural = 'Вкладка: УСЛУГИ'
		verbose_name = 'Наименование услуги'

		def __str__(self):
			return self.title
