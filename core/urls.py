from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('company/', views.company_view, name='company'),
    path('community/', views.community_view, name='community'),
    path('partners/', views.partners_view, name='partners'),
]
