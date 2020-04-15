import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'detail.html', {'mineral': mineral})


def random_mineral(request):
    minerals = Mineral.objects.all()
    pk = random.choice(minerals).pk
    return redirect('detail', pk=pk)
