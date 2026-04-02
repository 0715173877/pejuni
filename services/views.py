from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    context = {'services': Service.objects.all()}
    return render(request, 'services/list.html', context)

def service_detail(request, pk):
    context = {'service': get_object_or_404(Service, pk=pk)}
    return render(request, 'services/detail.html', context)
