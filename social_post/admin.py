from django.contrib import admin
from .models import SocialPost, Like, Comment
# Register your models here.

class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')


admin.site.register(SocialPost, SocialPostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
