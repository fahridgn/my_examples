from django import forms
from .models import Notlar

class NotForm(forms.ModelForm):
    class Meta:
        model = Notlar
        fields = ['baslik', 'icerik']
        exclude = ['ekleme_tarihi','author']