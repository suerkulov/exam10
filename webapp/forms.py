from django import forms
from webapp.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ['created_at', 'last_update', 'publicated_at', 'author', 'status']


class ModeratorForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['status']

