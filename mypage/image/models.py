from django.db import models

class Photos(models.Model):
    title = models.CharField(max_length=500, verbose_name = 'Наименования объекта')
    index = models.IntegerField(verbose_name = 'Номер')
    image = models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ')
    image_1= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_1')
    image_2= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_2')
    image_3= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_3')
    image_4= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_4',blank=True,null=True,)
    image_5= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_5',blank=True,null=True,)
    image_6= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_6',blank=True,null=True,)
    image_7= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_7',blank=True,null=True,)
    image_8= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_8',blank=True,null=True,)
    image_9= models.ImageField(upload_to='images',verbose_name = 'ИЗОБРАЖЕНИЕ_9',blank=True,null=True,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name = 'ДАТА')
    top = models.ForeignKey('Photos',on_delete=models.CASCADE,blank=True,null=True, verbose_name = 'Вывод названия объекта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Меню вкладки: НАШИ РАБОТЫ'
        verbose_name = 'НАШИ РАБОТЫ'
