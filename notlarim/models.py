from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

class Notlar(models.Model):
  baslik = models.CharField(max_length=200, verbose_name='Başlık')
  icerik = models.TextField(verbose_name='İçerik')
  date   = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tarih')
  yazar  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Yazar')
  

  def __str__(self):
    return self.icerik
  
  def get_absolute_url(self):
    return reverse("not_detay", kwargs={"pk": self.pk})






#class Comment(models.Model):
#    article = models.ForeignKey(Notlar, verbose_name=("Makale"), on_delete=models.CASCADE, related_name='comments')
#    comment = models.CharField(max_length=160, verbose_name=("Yorum") )
#    author  = models.ForeignKey(get_user_model(), verbose_name=("Yazar"), on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.comment
#    
#    def get_absolute_url(self):
#        return reverse('notlari_listele')