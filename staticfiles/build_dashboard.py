import os

# Define the models configuration
APPS = {
    'services': {
        'model': 'Service',
        'form': 'ServiceForm'
    },
    'projects': {
        'model': 'Project',
        'form': 'ProjectForm'
    },
    'team': {
        'model': 'TeamMember',
        'form': 'TeamMemberForm'
    },
    'news': {
        'model': 'Article',
        'form': 'ArticleForm'
    }
}

BASE_DIR = "."

def build_dashboard_views():
    for app, config in APPS.items():
        model = config['model']
        form = config['form']
        content = f"""from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import {model}
from .forms import {form}

class {model}ListView(LoginRequiredMixin, ListView):
    model = {model}
    template_name = 'dashboard/{app}/list.html'
    context_object_name = 'objects'

class {model}CreateView(LoginRequiredMixin, CreateView):
    model = {model}
    form_class = {form}
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:{app}_list')
    extra_context = {{'title': 'Create {model}'}}

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class {model}UpdateView(LoginRequiredMixin, UpdateView):
    model = {model}
    form_class = {form}
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:{app}_list')
    extra_context = {{'title': 'Edit {model}'}}

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class {model}DeleteView(LoginRequiredMixin, DeleteView):
    model = {model}
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:{app}_list')
    extra_context = {{'title': 'Delete {model}'}}
"""
        with open(os.path.join(BASE_DIR, app, 'dashboard_views.py'), 'w') as f:
            f.write(content)
        print(f"Generated {app}/dashboard_views.py")

def build_core_views():
    content = """from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_count'] = Service.objects.count()
        context['projects_count'] = Project.objects.count()
        context['team_count'] = TeamMember.objects.count()
        context['news_count'] = Article.objects.count()
        return context

class DashLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True
"""
    with open(os.path.join(BASE_DIR, 'core', 'dashboard_views.py'), 'w') as f:
        f.write(content)
    print("Generated core/dashboard_views.py")

def build_urls():
    content = """from django.urls import path
from django.contrib.auth.views import LogoutView
from core.dashboard_views import DashboardHomeView, DashLoginView
from services.dashboard_views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView
from projects.dashboard_views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from team.dashboard_views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView
from news.dashboard_views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    path('login/', DashLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/dashboard/login/'), name='logout'),

    # Services
    path('services/', ServiceListView.as_view(), name='services_list'),
    path('services/add/', ServiceCreateView.as_view(), name='services_add'),
    path('services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='services_edit'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='services_delete'),

    # Projects
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='projects_add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='projects_edit'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='projects_delete'),

    # Team
    path('team/', TeamMemberListView.as_view(), name='team_list'),
    path('team/add/', TeamMemberCreateView.as_view(), name='team_add'),
    path('team/<int:pk>/edit/', TeamMemberUpdateView.as_view(), name='team_edit'),
    path('team/<int:pk>/delete/', TeamMemberDeleteView.as_view(), name='team_delete'),

    # News
    path('news/', ArticleListView.as_view(), name='news_list'),
    path('news/add/', ArticleCreateView.as_view(), name='news_add'),
    path('news/<int:pk>/edit/', ArticleUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', ArticleDeleteView.as_view(), name='news_delete'),
]
"""
    with open(os.path.join(BASE_DIR, 'core', 'dashboard_urls.py'), 'w') as f:
        f.write(content)
    print("Generated core/dashboard_urls.py")

if __name__ == '__main__':
    build_dashboard_views()
    build_core_views()
    build_urls()
