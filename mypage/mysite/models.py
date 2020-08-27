from django.db import models

class Contact(models.Model):
    names = models.CharField(max_length=500,  verbose_name = "Имя",)
    email = models.CharField(max_length=500,  verbose_name = "Почта",)
    text = models.CharField(max_length=500, blank=True, null = True, verbose_name = "Дополнительное поле",)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Меню вкладки: КОНТАКТЫ"
        verbose_name = "КОНТАКТЫ"

    def __str__(self):
        return self.names
