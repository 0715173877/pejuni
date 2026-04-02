from django.contrib import admin
from .models import Service
from core.admin import AuditAdminMixin

@admin.register(Service)
class ServiceAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at', 'updated_by')
    search_fields = ('title', 'description', 'full_description')
