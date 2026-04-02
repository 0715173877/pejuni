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

from .models import Advantage, HeroContent

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


