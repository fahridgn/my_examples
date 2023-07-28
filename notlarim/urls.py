from django.contrib import admin
from django.urls import path,include
from .views import NotlarListView, NotEkleView, NotDetayView, NotGuncelleView, NotSilView


urlpatterns = [
    path('', NotlarListView.as_view(), name='notlar_list'),
    path('not-ekle/', NotEkleView.as_view(), name='not_ekle'),
    path('<int:pk>/', NotDetayView.as_view(), name='not_detay'),
    path('<int:pk>/guncelle/', NotGuncelleView.as_view(), name='not_guncelle'),
    path('<int:pk>/sil/', NotSilView.as_view(), name='not_sil'),
]