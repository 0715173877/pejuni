from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'bio', 'cv', 'image', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
