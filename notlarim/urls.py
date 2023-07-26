from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('', views.NotlarimView.as_view(), name='notlari_listele'),
    path('not_ekle/', views.YeniNot.as_view(), name="icerik"),
    path('not_detay/<int:pk>/', views.NotDetay.as_view(), name='not_detay'),
    path('notlarim/<int:pk>/duzenle/', views.NotDuzenle.as_view(), name='not_duzenle'),
    path('notlarim/<int:pk>/uye_sil/', views.NotSil.as_view(), name="not_sil"),
] 