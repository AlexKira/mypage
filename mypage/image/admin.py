from django.contrib import admin
from .models import NewsWork


class NewsWorkInline(admin.TabularInline):
    model = NewsWork

@admin.register(NewsWork)
class NewsWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'status', 'date_added')
    list_display_links = ('title', 'img', 'status', 'date_added')
    inlines = [NewsWorkInline]
