from django.contrib import admin
from .models import Article
from core.admin import AuditAdminMixin

@admin.register(Article)
class ArticleAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'date', 'order', 'updated_at', 'updated_by')
    ordering = ('-date',)
