from django.db import models
from core.models import AuditModel

class Project(AuditModel):
    COUNTRY_OPTIONS = [
        ('Tanzania', 'Tanzania'),
        ('Kenya', 'Kenya'),
        ('Uganda', 'Uganda'),
        ('Rwanda', 'Rwanda'),
        ('Burundi', 'Burundi'),
        ('DRC', 'Democratic Republic of the Congo'),
        ('Zambia', 'Zambia'),
        ('Malawi', 'Malawi'),
        ('Mozambique', 'Mozambique'),
        ('South Africa', 'South Africa'),
        ('Nigeria', 'Nigeria'),
        ('Ghana', 'Ghana'),
        ('Angola', 'Angola'),
        ('Namibia', 'Namibia'),
        ('Botswana', 'Botswana'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Other', 'Other/Global')
    ]

    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100, choices=COUNTRY_OPTIONS, blank=True, null=True, help_text="Select the country where this project took place.")
    description = models.TextField()
    detailed_scope = models.TextField(blank=True, null=True, help_text="Extensive project scope and methodology for the detail page.")
    detailed_scope = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title
