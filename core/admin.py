from django.contrib import admin
from .models import Partner, Testimonial

class AuditAdminMixin:
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(Partner)
class PartnerAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'order', 'updated_at', 'updated_by')

@admin.register(Testimonial)
class TestimonialAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('author', 'stars', 'order', 'updated_at')
