from django.contrib import admin
from .models import Project
from core.admin import AuditAdminMixin

@admin.register(Project)
class ProjectAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at', 'updated_by')
    ordering = ('order',)
