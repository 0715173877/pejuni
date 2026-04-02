from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service
from .forms import ServiceForm

class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'dashboard/services/list.html'
    context_object_name = 'objects'

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Service'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('services:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:services_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Service'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('services:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:services_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:services_list')
    extra_context = {'title': 'Delete Service'}
