from django.db import models
from django.contrib.auth import get_user_model
from notlarim.models import Notlar

class Yorumlar(models.Model):
    notlar = models.ForeignKey(Notlar, on_delete=models.CASCADE)
    yazar = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.icerik