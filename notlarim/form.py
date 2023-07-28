from django import forms
from .models import Notlar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class NotForm(forms.ModelForm):
    class Meta:
        model = Notlar
        fields = ['baslik', 'icerik']
        exclude = ['ekleme_tarihi','yazar']

    def __init__(self, *args, **kwargs):
        super(NotForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'baslik',
            'icerik',
            Submit('submit', 'icerik')
        )