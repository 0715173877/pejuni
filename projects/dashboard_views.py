from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'dashboard/projects/list.html'
    context_object_name = 'objects'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Project'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('projects:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:projects_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Project'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('projects:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:projects_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:projects_list')
    extra_context = {'title': 'Delete Project'}
