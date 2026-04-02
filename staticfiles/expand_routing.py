import os

base_dir = "../pejuni.com "

files = {
    "pejuni_config/urls.py": """from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
    path('people/', include('team.urls')),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
""",
    "core/urls.py": """from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('company/', views.company_view, name='company'),
    path('community/', views.community_view, name='community'),
    path('partners/', views.partners_view, name='partners'),
]
""",
    "core/views.py": """from django.shortcuts import render
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Partner, Testimonial, Statistic

def home(request):
    context = {
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'team_members': TeamMember.objects.all(),
        'articles': Article.objects.all(),
        'partners': Partner.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'statistics': Statistic.objects.all(),
    }
    return render(request, 'index.html', context)

def company_view(request):
    return render(request, 'core/company.html')

def community_view(request):
    return render(request, 'core/community.html')

def partners_view(request):
    context = {'partners': Partner.objects.all()}
    return render(request, 'core/partners.html', context)
""",
    "services/urls.py": """from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='list'),
    path('<int:pk>/', views.service_detail, name='detail'),
]
""",
    "services/views.py": """from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    context = {'services': Service.objects.all()}
    return render(request, 'services/list.html', context)

def service_detail(request, pk):
    context = {'service': get_object_or_404(Service, pk=pk)}
    return render(request, 'services/detail.html', context)
""",
    "projects/urls.py": """from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='list'),
    path('<int:pk>/', views.project_detail, name='detail'),
]
""",
    "projects/views.py": """from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'projects/list.html', context)

def project_detail(request, pk):
    context = {'project': get_object_or_404(Project, pk=pk)}
    return render(request, 'projects/detail.html', context)
""",
    "team/urls.py": """from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team_list, name='list'),
    path('<int:pk>/', views.team_detail, name='detail'),
]
""",
    "team/views.py": """from django.shortcuts import render, get_object_or_404
from .models import TeamMember

def team_list(request):
    context = {'team_members': TeamMember.objects.all()}
    return render(request, 'team/list.html', context)

def team_detail(request, pk):
    context = {'member': get_object_or_404(TeamMember, pk=pk)}
    return render(request, 'team/detail.html', context)
""",
    "news/urls.py": """from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:pk>/', views.article_detail, name='detail'),
]
""",
    "news/views.py": """from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'news/list.html', context)

def article_detail(request, pk):
    context = {'article': get_object_or_404(Article, pk=pk)}
    return render(request, 'news/detail.html', context)
"""
}

def inject_field(filepath, search_target, new_field):
    target = os.path.join(base_dir, filepath)
    if os.path.exists(target):
        with open(target, 'r') as f:
            content = f.read()
        if new_field not in content:
            content = content.replace(search_target, f"{search_target}\n    {new_field}")
            with open(target, 'w') as f:
                f.write(content)
            print(f"Injected field into {filepath}")

# Process Models (Injecting TextField attributes for detail pages)
inject_field("services/models.py", "description = models.TextField()", "full_description = models.TextField(blank=True, null=True, help_text=\"Detailed text to render on the specific service page.\")")
inject_field("projects/models.py", "description = models.TextField()", "detailed_scope = models.TextField(blank=True, null=True, help_text=\"Extensive project scope and methodology for the detail page.\")")
inject_field("team/models.py", "role = models.CharField(max_length=200)", "bio = models.TextField(blank=True, null=True, help_text=\"Full professional biography for the detail profile.\")")
inject_field("news/models.py", "link = models.URLField(blank=True, null=True)", "content = models.TextField(blank=True, null=True, help_text=\"Complete article body text.\")")

for filepath, content in files.items():
    target = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully configured: {target}")

print("----------")
print("CMS Multi-Page Database and Routing Infrastructure successfully expanded.")
