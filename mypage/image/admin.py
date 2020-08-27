from django.contrib import admin
from image.models import Photos
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('index',
                    'title',
                    'top',
                    'image',
                    'timestamp',)
search_fields = ('title', 'top', 'index')
