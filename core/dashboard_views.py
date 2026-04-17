from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Statistic, Advantage, HeroContent, FooterContent, Partner, Testimonial
from core.forms import StatisticForm, AdvantageForm, UserProfileForm, HeroContentForm, DashboardUserForm, FooterContentForm, PartnerForm, TestimonialForm
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

class ManageHeroView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HeroContent
    form_class = HeroContentForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:hero')
    success_message = "Hero section updated successfully."
    extra_context = {'title': 'Manage Hero Content'}

    def get_object(self, queryset=None):
        obj, created = HeroContent.objects.get_or_create(id=1)
        if created and hasattr(obj, 'created_by'):
            obj.created_by = self.request.user
            obj.save()
        return obj

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ManageFooterView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FooterContent
    form_class = FooterContentForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:footer')
    success_message = "Footer section updated successfully."
    extra_context = {'title': 'Manage Footer Content'}

    def get_object(self, queryset=None):
        obj, created = FooterContent.objects.get_or_create(id=1)
        if created and hasattr(obj, 'created_by'):
            obj.created_by = self.request.user
            obj.save()
        return obj

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class ManageFooterView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FooterContent
    form_class = FooterContentForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:footer')
    success_message = "Global footer configuration updated successfully."
    extra_context = {'title': 'Manage Footer Configuration'}

    def get_object(self, queryset=None):
        obj, created = FooterContent.objects.get_or_create(id=1)
        if created and hasattr(obj, 'created_by'):
            obj.created_by = self.request.user
            obj.save()
        return obj

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class DashboardPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:profile')
    success_message = "Your password was updated successfully."
    extra_context = {'title': 'Change Password'}

class DashboardUserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users/list.html'
    context_object_name = 'objects'

class DashboardUserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = DashboardUserForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:users_list')
    success_message = "User created successfully with default password 'ChangeMe@2026!'."
    extra_context = {'title': 'Create New User', 'help_msg': 'The user will be automatically assigned the password: ChangeMe@2026!'}

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password('ChangeMe@2026!')
        user.save()
        return super().form_valid(form)

class DashboardUserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = DashboardUserForm
    template_name = 'dashboard/shared_form.html'
    success_url = reverse_lazy('dashboard:users_list')
    success_message = "User profile updated successfully."
    extra_context = {'title': 'Edit User'}

class DashboardUserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:users_list')
    extra_context = {'title': 'Delete User Account'}

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

class PartnerListView(LoginRequiredMixin, ListView):
    model = Partner
    template_name = 'dashboard/partners/list.html'
    context_object_name = 'objects'

class PartnerCreateView(LoginRequiredMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Partner'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:partners_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class PartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Partner'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:partners_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class PartnerDeleteView(LoginRequiredMixin, DeleteView):
    model = Partner
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:partners_list')
    extra_context = {'title': 'Delete Partner'}

class TestimonialListView(LoginRequiredMixin, ListView):
    model = Testimonial
    template_name = 'dashboard/testimonials/list.html'
    context_object_name = 'objects'

class TestimonialCreateView(LoginRequiredMixin, CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Create Testimonial'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:testimonials_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'created_by'):
            form.instance.created_by = self.request.user
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class TestimonialUpdateView(LoginRequiredMixin, UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'dashboard/shared_form.html'
    extra_context = {'title': 'Edit Testimonial'}

    def get_success_url(self):
        if '_save_and_preview' in self.request.POST:
            return reverse_lazy('core:home')
        return reverse_lazy('dashboard:testimonials_list')

    def form_valid(self, form):
        if hasattr(form.instance, 'updated_by'):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class TestimonialDeleteView(LoginRequiredMixin, DeleteView):
    model = Testimonial
    template_name = 'dashboard/shared_confirm_delete.html'
    success_url = reverse_lazy('dashboard:testimonials_list')
    extra_context = {'title': 'Delete Testimonial'}


