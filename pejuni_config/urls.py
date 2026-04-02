from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),  # Disabled per client request
    path('dashboard/', include('core.dashboard_urls')),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
    path('people/', include('team.urls')),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
