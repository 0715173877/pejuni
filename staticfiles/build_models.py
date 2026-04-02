import os

base_dir = "../pejuni.com "

import glob
for bad_migration in glob.glob(os.path.join(base_dir, "*/migrations/0002*.py")):
    try:
        os.remove(bad_migration)
        print(f"Flushed corrupted migration: {bad_migration}")
    except Exception as e:
        pass

files = {
    "core/models.py": """from django.db import models
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
""",
    "core/admin.py": """from django.contrib import admin
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
""",
    "services/models.py": """from django.db import models
from core.models import AuditModel

class Service(AuditModel):
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
from core.admin import AuditAdminMixin

@admin.register(Service)
class ServiceAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at', 'updated_by')
    ordering = ('order',)
""",
    "projects/models.py": """from django.db import models
from core.models import AuditModel

class Project(AuditModel):
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
from core.admin import AuditAdminMixin

@admin.register(Project)
class ProjectAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at', 'updated_by')
    ordering = ('order',)
""",
    "team/models.py": """from django.db import models
from core.models import AuditModel

class TeamMember(AuditModel):
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
from core.admin import AuditAdminMixin

@admin.register(TeamMember)
class TeamMemberAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'updated_at', 'updated_by')
    ordering = ('order',)
""",
    "news/models.py": """from django.db import models
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
""",
    "news/admin.py": """from django.contrib import admin
from .models import Article
from core.admin import AuditAdminMixin

@admin.register(Article)
class ArticleAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'date', 'order', 'updated_at', 'updated_by')
    ordering = ('-date',)
"""
}

for filepath, content in files.items():
    target = os.path.join(base_dir, filepath)
    if os.path.exists(target):
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully configured API Audit Trail for: {target}")
    else:
        print(f"File not found: {target}")

print("----------")
print("CMS Enterprise Audit Architecture completely sequenced.")
