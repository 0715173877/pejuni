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

from .models import Advantage

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

