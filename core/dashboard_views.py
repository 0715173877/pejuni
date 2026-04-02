from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Statistic, Advantage
from core.forms import StatisticForm, AdvantageForm, UserProfileForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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

class DashboardProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:profile')
    success_message = "Your profile was updated successfully."
    extra_context = {'title': 'My Profile'}

    def get_object(self, queryset=None):
        return self.request.user

class DashboardPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:profile')
    success_message = "Your password was updated successfully."
    extra_context = {'title': 'Change Password'}

class StatisticListView(LoginRequiredMixin, ListView):
    model = Statistic
    template_name = 'dashboard/statistics/list.html'
    context_object_name = 'objects'

class StatisticCreateView(LoginRequiredMixin, CreateView):
    model = Statistic
    form_class = StatisticForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Statistic'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home') # Statistics show on the home page
        return reverse_lazy('dashboard:statistics_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class StatisticUpdateView(LoginRequiredMixin, UpdateView):
    model = Statistic
    form_class = StatisticForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Statistic'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:statistics_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class StatisticDeleteView(LoginRequiredMixin, DeleteView):
    model = Statistic
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:statistics_list')
    extra_context = {'title': 'Delete Statistic'}

class AdvantageListView(LoginRequiredMixin, ListView):
    model = Advantage
    template_name = 'dashboard/advantages/list.html'
    context_object_name = 'objects'

class AdvantageCreateView(LoginRequiredMixin, CreateView):
    model = Advantage
    form_class = AdvantageForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Advantage (Why Choose Us)'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:advantages_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class AdvantageUpdateView(LoginRequiredMixin, UpdateView):
    model = Advantage
    form_class = AdvantageForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Advantage'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:advantages_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class AdvantageDeleteView(LoginRequiredMixin, DeleteView):
    model = Advantage
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:advantages_list')
    extra_context = {'title': 'Delete Advantage'}

