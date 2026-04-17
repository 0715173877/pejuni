from django import forms
from .models import Statistic

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['label', 'value_number', 'value_suffix', 'order']
        widgets = {
            'label': forms.TextInput(attrs={'class': 'form-control'}),
            'value_number': forms.TextInput(attrs={'class': 'form-control'}),
            'value_suffix': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from .models import Advantage, HeroContent, FooterContent

class FooterContentForm(forms.ModelForm):
    class Meta:
        model = FooterContent
        fields = ['company_description', 'address_hq', 'phone_hq', 'phone_aus', 'email_primary', 'email_secondary', 'linkedin_url', 'twitter_url']
        widgets = {
            'company_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'address_hq': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'phone_hq': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_aus': forms.TextInput(attrs={'class': 'form-control'}),
            'email_primary': forms.EmailInput(attrs={'class': 'form-control'}),
            'email_secondary': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
        }

class HeroContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = ['kicker', 'title', 'description', 'background_image', 'intro_statement', 'why_choose_us_intro']
        widgets = {
            'kicker': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'help_text': 'Use <br> for line breaks.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'intro_statement': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'why_choose_us_intro': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'background_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

from .models import Partner, Testimonial, FooterContent

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'logo_domain', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo_domain': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author', 'quote', 'stars', 'order']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'stars': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FooterContentForm(forms.ModelForm):
    class Meta:
        model = FooterContent
        fields = ['company_description', 'address_hq', 'phone_hq', 'phone_aus', 'email_primary', 'email_secondary', 'linkedin_url', 'twitter_url']
        widgets = {
            'company_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'address_hq': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'phone_hq': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_aus': forms.TextInput(attrs={'class': 'form-control'}),
            'email_primary': forms.EmailInput(attrs={'class': 'form-control'}),
            'email_secondary': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class AdvantageForm(forms.ModelForm):
    class Meta:
        model = Advantage
        fields = ['title', 'description', 'icon_number', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'icon_number': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class DashboardUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-top: 10px; transform: scale(1.5);'}),
        }


