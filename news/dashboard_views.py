from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import ArticleForm

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'dashboard/news/list.html'
    context_object_name = 'objects'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Article'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('news:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:news_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Article'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('news:detail', kwargs={'pk': self.object.pk})
        return reverse_lazy('dashboard:news_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:news_list')
    extra_context = {'title': 'Delete Article'}
