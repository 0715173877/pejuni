import os

base_dir = "../pejuni.com "

files = {
    "services/models.py": """from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title
""",
    "services/admin.py": """from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
""",
    "projects/models.py": """from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title
""",
    "projects/admin.py": """from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
""",
    "team/models.py": """from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name
""",
    "team/admin.py": """from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    ordering = ('order',)
""",
    "news/models.py": """from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date', 'order']
        
    def __str__(self):
        return self.title
""",
    "news/admin.py": """from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'order')
    ordering = ('-date',)
""",
    "core/models.py": """from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo_domain = models.URLField(help_text="e.g., https://barrick.com")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    author = models.CharField(max_length=200)
    quote = models.TextField()
    stars = models.IntegerField(default=5)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.author
""",
    "core/admin.py": """from django.contrib import admin
from .models import Partner, Testimonial

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_domain', 'order')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'stars', 'order')
"""
}

for filepath, content in files.items():
    target = os.path.join(base_dir, filepath)
    if os.path.exists(target):
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully configured: {target}")
    else:
        print(f"File not found: {target}")

print("----------")
print("CMS Database Models completely orchestrated.")
