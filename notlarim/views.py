from django.shortcuts import render
from django.views import generic
from .models import Notlar
from django.urls import reverse_lazy
from django.forms import Form


class NotlarimView(generic.ListView):
    model= Notlar
    form= Form
    template_name='notlari_listele.html'


class NotDetay(generic.DetailView):
    model=Notlar
    template_name='not_detay.html'


class YeniNot(generic.edit.CreateView):
    model = Notlar
    template_name='yeni_not.html'
    fields = '__all__'

class NotSil(generic.edit.DeleteView):
    model = Notlar
    template_name='not_sil.html'
    success_url=reverse_lazy("notlari_listele") #notlari_listele bi template değil urls patternde tanımlı listview değişkenidir. Bkz.urls.py 6. satır

class NotDuzenle(generic.edit.UpdateView):
    model = Notlar
    template_name='not_duzenle.html'
    fields = ['baslik','icerik']
