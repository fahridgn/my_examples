from django.contrib import admin
from .models import Notlar

# Register your models here.

class NotlarimAdmin(admin.ModelAdmin):
  list_display = ("baslik", "icerik") #admin panelinde başlık ve içerik şeklinde görünmesi için listele komutu
  
admin.site.register(Notlar, NotlarimAdmin)