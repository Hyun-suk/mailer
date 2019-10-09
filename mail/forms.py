from django import forms
from .models import Marketing, Settings

class MarketingForm(forms.ModelForm):
    class Meta:
        model = Marketing
        fields = ['name' , 'content']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['email', 'smtp_key']

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
            'smtp_key': forms.TextInput(attrs={'placeholder': 'Enter your smtp password'}),
        }
