from django import forms
from .models import Yorumlar

class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorumlar
        fields = ['notlar', 'yazar', 'icerik']