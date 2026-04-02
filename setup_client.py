import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pejuni_config.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from core.models import Partner, Testimonial, Statistic
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article

print("Initializing Client Dashboard Configurations...")

# Create or get the Client group
client_group, created = Group.objects.get_or_create(name='Content Editors')

# Models that the client should be able to edit
editable_models = [Partner, Testimonial, Statistic, Service, Project, TeamMember, Article]

# Clear existing permissions (if rerunning)
client_group.permissions.clear()

# Add all CRUD permissions dynamically
for model in editable_models:
    content_type = ContentType.objects.get_for_model(model)
    permissions = Permission.objects.filter(content_type=content_type)
    for p in permissions:
        client_group.permissions.add(p)

print("SUCCESS: Established 'Content Editors' Group with strict CMS isolation.")

# Create the standard client user
if not User.objects.filter(username='pejuniclient').exists():
    client_user = User.objects.create_user('pejuniclient', 'client@pejuni.com', 'pejuni2026')
    client_user.is_staff = True # Required for logging into the /admin portal
    client_user.save()
    client_user.groups.add(client_group)
    print("\n--- NEW CLIENT ACCESS CREDENTIALS ---")
    print("URL: http://127.0.0.1:8000/admin")
    print("Username: pejuniclient")
    print("Password: pejuni2026")
    print("-------------------------------------")
    print("This user can exclusively access and edit the website contents. They CANNOT edit templates, user credentials, or system settings.")
else:
    print("Client account 'pejuniclient' already exists.")
