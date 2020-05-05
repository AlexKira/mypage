from django.contrib import admin

# Register your models here.
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date_added')
    list_display_links = ('title','text')
    search_fields = ('title', 'text')

admin.site.register(Service,ServiceAdmin)
