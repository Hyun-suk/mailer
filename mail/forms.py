from django import forms
from .models import Marketing, Settings
from django.utils.translation import ugettext_lazy as _

class MarketingForm(forms.ModelForm):
    class Meta:
        model = Marketing
        fields = ['name' , 'content']

class AddressForm(forms.ModelForm):
    from_mail = forms.ModelChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

        self.fields['from_mail'].label = _("보내는 주소")
        self.fields['from_mail'].queryset = user.settings
        self.fields['from_mail'].initial = user.settings.first()

    class Meta:
        model = Settings
        fields = ['from_mail']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['email', 'smtp_key']

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
            'smtp_key': forms.TextInput(attrs={'placeholder': 'Enter your smtp password'}),
        }
