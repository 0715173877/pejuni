from django.db import models
from core.models import AuditModel

class TeamMember(AuditModel):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True, help_text="Full professional biography for the detail profile.")
    cv = models.FileField(upload_to='team_cvs/', blank=True, null=True, help_text="Upload the member's CV (PDF recommended)")
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name
