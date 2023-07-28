from django.urls import path
from . import views

urlpatterns = [
    path('<int:not_id>/', views.yorum_list, name='yorum_list'),
    path('<int:not_id>/yorum_ekle/', views.yorum_ekle, name='yorum_ekle'),
    path('<int:not_id>/yorum_guncelle/<int:yorum_id>/', views.yorum_guncelle, name='yorum_guncelle'),
    path('<int:not_id>/yorum_sil/<int:yorum_id>/', views.yorum_sil, name='yorum_sil'),
]