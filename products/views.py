from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from .models import Kirim
from django.shortcuts import redirect
from .form import KirimForm

def kirim_list(request):
    kirims = Kirim.objects.filter(arrival_date__lte=timezone.now()).order_by('arrival_date')
    return render(request, 'products/kirim_list.html', {'kirims': kirims})

def kirim_detail(request, pk):
    kirim = get_object_or_404(Kirim, pk=pk)
    return render(request, 'products/kirim_detail.html', {'kirim': kirim})
    pass

def kirim_new(request):
    if request.method == 'POST':
        form = KirimForm(request.POST)
        if form.is_valid():
            kirim = form.save(commit=False)
            kirim.author = request.user
            kirim.save()
            return redirect('kirim_detail', pk=kirim.pk)
    else:
        form = KirimForm()
    return render(request, 'products/kirim_edit.html', {'form': form})


def kirim_edit(request, pk):
    kirim = get_object_or_404(Kirim, pk=pk)
    if request.method == 'POST':
        form = KirimForm(request.POST, instance=kirim)
        if form.is_valid():
            kirim = form.save(commit=False)
            kirim.author = request.user
            kirim.save()
            return redirect('kirim_detail', pk=kirim.pk)
    else:
        form = KirimForm(instance=kirim)
    return render(request, 'products/kirim_edit.html', {'form': form})