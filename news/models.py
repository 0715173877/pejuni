from django.db import models
from core.models import AuditModel

class Article(AuditModel):
    title = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date', 'order']
        
    def __str__(self):
        return self.title
