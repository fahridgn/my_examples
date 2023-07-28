from django.shortcuts import render, get_object_or_404, redirect
from .models import Yorumlar
from .forms import YorumForm

def yorum_list(request, not_id):
    yorumlar = Yorumlar.objects.filter(notlar_id=not_id)
    return render(request, 'yorumlar/yorum_list.html', {'yorumlar': yorumlar})

def yorum_detay(request, pk):
    yorum = get_object_or_404(Yorumlar, pk=pk)
    return render(request, 'yorumlar/yorum_detay.html', {'yorum': yorum})

def yorum_ekle(request):
    if request.method == 'POST':
        form = YorumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yorum_list')
    else:
        form = YorumForm()
    return render(request, 'yorumlar/yorum_ekle.html', {'form': form})

def yorum_guncelle(request, pk):
    yorum = get_object_or_404(Yorumlar, pk=pk)
    if request.method == 'POST':
        form = YorumForm(request.POST, instance=yorum)
        if form.is_valid():
            form.save()
            return redirect('yorum_detay', pk=pk)
    else:
        form = YorumForm(instance=yorum)
    return render(request, 'yorumlar/yorum_guncelle.html', {'form': form})

def yorum_sil(request, pk):
    yorum = get_object_or_404(Yorumlar, pk=pk)
    if request.method == 'POST':
        yorum.delete()
        return redirect('yorum_list')
    return render(request, 'yorumlar/yorum_sil.html', {'yorum': yorum})
