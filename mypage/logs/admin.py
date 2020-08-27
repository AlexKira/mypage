from django.contrib import admin
from logs.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','body', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
