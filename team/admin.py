from django.contrib import admin
from .models import TeamMember
from core.admin import AuditAdminMixin

@admin.register(TeamMember)
class TeamMemberAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'updated_at', 'updated_by')
    search_fields = ('name', 'role', 'bio')
