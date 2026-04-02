from django.db import models
from core.models import AuditModel

class Service(AuditModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    full_description = models.TextField(blank=True, null=True, help_text="Detailed text to render on the specific service page.")
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title
