from django.db import models
# Create your models here.
class NewsWork(models.Model):
    title = models.CharField(max_length=600, blank=True)
    date_added=models.DateField(null=True, blank=True)
    img=models.ImageField(upload_to='image')
    author = models.ForeignKey('NewsWork', models.SET_NULL,blank=True, null=True)

    LOAN_STATUS = (
        ('m', 'main'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')



    def __str__(self):
        return self.title
        return self.author
        return self.status
