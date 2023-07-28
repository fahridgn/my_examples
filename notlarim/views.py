# notlarim/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Notlar

class NotlarListView(ListView):
    model = Notlar
    template_name = 'notlarim/notlar_list.html'
    context_object_name = 'notlar'

class NotDetayView(DetailView):
    model = Notlar
    template_name = 'notlarim/not_detay.html'
    context_object_name = 'not'

class NotEkleView(CreateView):
    model = Notlar
    template_name = 'notlarim/not_ekle.html'
    fields = ['baslik', 'icerik']
    success_url = reverse_lazy('notlar_list')

    def form_valid(self, form):
        form.instance.yazar = self.request.user
        return super().form_valid(form)

class NotGuncelleView(UpdateView):
    model = Notlar
    template_name = 'notlarim/not_guncelle.html'
    fields = ['baslik', 'icerik']

class NotSilView(DeleteView):
    model = Notlar
    template_name = 'notlarim/not_sil.html'
    success_url = reverse_lazy('notlar_list')

