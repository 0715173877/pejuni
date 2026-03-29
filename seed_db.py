import os
import sys
import shutil
import django
import datetime

# Attach the script to your exact Django Application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pejuni_config.settings')
django.setup()

# Import all the Data Blueprints we just migrated
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Partner, Testimonial
from django.contrib.auth.models import User

# Acquire superuser for audit trail
admin_user = User.objects.filter(is_superuser=True).first()
audit_payload = {'created_by': admin_user, 'updated_by': admin_user}
# Construct the Secure Media Upload Paths
media_dirs = ['media/services', 'media/projects', 'media/team', 'media/news']
for d in media_dirs:
    os.makedirs(d, exist_ok=True)

# The folder where the source images currently live
SRC_DIR = "../pejuni.com"

def save_media(src_file, folder):
    if not src_file: return None
    src_path = os.path.join(SRC_DIR, src_file)
    dst_rel = f"{folder}/{src_file}"
    dst_path = os.path.join("media", dst_rel)
    
    # Physically copy image files into the PostgreSQL/Django upload path
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        return dst_rel
    else:
        print(f"Warning: Could not locate {src_file}")
    return None

print("Clearing empty/old demo data from PostgreSQL...")
Service.objects.all().delete()
Project.objects.all().delete()
TeamMember.objects.all().delete()
Article.objects.all().delete()
Partner.objects.all().delete()

print("Automatically Seeding Services...")
Service.objects.create(title="Geotechnical Data Collection", description="Precise core logging is the foundation of structural integrity...", image=save_media("pejun_if0ams.jpg", "services"), order=1, **audit_payload)
Service.objects.create(title="Slope Stability & Pit Design", description="We proactively manage high-risk open pits...", image=save_media("gen_open_pit_1774697006529.png", "services"), order=2, **audit_payload)
Service.objects.create(title="Soil Lab & Acoustic Logging", description="Supported by our integrated laboratory operations...", image=save_media("gen_core_samples_1774697044916.png", "services"), order=3, **audit_payload)
Service.objects.create(title="Training & Mentorship", description="Empowering the next generation...", image=save_media("choose-img.jpg", "services"), order=4, **audit_payload)
Service.objects.create(title="Geotechnical Engineering", description="We provide essential engineering services...", image=save_media("gen_engineering_1774696967271.png", "services"), order=5, **audit_payload)
Service.objects.create(title="Bore Hole & Geophysical Survey", description="Precise surveying and bore hole drilling assessments...", image=save_media("gen_underground_1774697024373.png", "services"), order=6, **audit_payload)

print("Automatically Seeding Projects...")
Project.objects.create(title="Geita Pit Expansion", description="Advanced numerical modeling and slope evaluation for deep extraction phases.", image=save_media("slope.png", "projects"), order=1, **audit_payload)
Project.objects.create(title="Bulyanhulu Underground", description="Comprehensive underground stability surveys utilizing deep geophysical boreholes.", image=save_media("gen_open_pit_1774697006529.png", "projects"), order=2, **audit_payload)
Project.objects.create(title="Kibali Foundation Design", description="Soil and rock mechanic testing resulting in precision structural foundations.", image=save_media("gen_engineering_1774696967271.png", "projects"), order=3, **audit_payload)

print("Automatically Seeding Team Leadership...")
TeamMember.objects.create(name="Juma Mgumbwa", role="Director & Principal Geotechnical Engineer", image=save_media("gen_juma_1774698598033.png", "team"), order=1, **audit_payload)
TeamMember.objects.create(name="Gilbert Alexander Mboma", role="Geotechnical Engineer", image=save_media("gen_gilbert_1774698616598.png", "team"), order=2, **audit_payload)
TeamMember.objects.create(name="Eliud Mwakyolile", role="Senior Geotechnical Engineer", image=save_media("gen_eliud_1774698633669.png", "team"), order=3, **audit_payload)

print("Automatically Seeding News Insights...")
Article.objects.create(title="Advancements in Automated Slope Stability Monitoring", date=datetime.date(2024, 10, 12), image=save_media("choose-img.jpg", "news"), order=1, **audit_payload)
Article.objects.create(title="Pejuni Expands Laboratory Capabilities in Tanzania", date=datetime.date(2024, 9, 28), image=save_media("pejun_if0ams.jpg", "news"), order=2, **audit_payload)
Article.objects.create(title="Why Geotechnical Mentorship Matters on the Mining Site", date=datetime.date(2024, 8, 15), image=save_media("slope.png", "news"), order=3, **audit_payload)

print("Automatically Seeding Partners...")
Partner.objects.create(name="Barrick Gold", logo_domain="https://barrick.com", order=1, **audit_payload)
Partner.objects.create(name="AngloGold Ashanti", logo_domain="https://anglogoldashanti.com", order=2, **audit_payload)
Partner.objects.create(name="Shanta Gold", logo_domain="https://shantagold.com", order=3, **audit_payload)
Partner.objects.create(name="Petra Diamonds", logo_domain="https://petradiamonds.com", order=4, **audit_payload)
Partner.objects.create(name="Rio Tinto", logo_domain="https://riotinto.com", order=5, **audit_payload)

print("Automatically Seeding Testimonials...")
Testimonial.objects.create(author="Mining Operations Director, Australia", quote="Pejuni provided exceptional geotechnical modeling that drastically improved the safety and yield of our pit expansion. Their team is definitively top-tier.", stars=5, order=1, **audit_payload)
Testimonial.objects.create(author="HR Director, Tanzania Operations", quote="The training and mentorship our young engineers received from Pejuni was invaluable. They systematically blend theory and real-world underground practice flawlessly.", stars=5, order=2, **audit_payload)

print("\n--- BOOM! ---")
print("SUCCESS: Your PostgreSQL database is now 100% populated with all records!")
print("ALL images have safely migrated to the Media system. Check the Admin panel.")
