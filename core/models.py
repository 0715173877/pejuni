from django.db import models
from django.contrib.auth.models import User

class AuditModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_%(class)s_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_%(class)s_updated")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Partner(AuditModel):
    name = models.CharField(max_length=100)
    logo_domain = models.URLField(help_text="e.g., https://barrick.com")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

class Testimonial(AuditModel):
    author = models.CharField(max_length=200)
    quote = models.TextField()
    stars = models.IntegerField(default=5)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.author
