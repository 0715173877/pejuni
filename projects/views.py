from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'projects/list.html', context)

def project_detail(request, pk):
    context = {'project': get_object_or_404(Project, pk=pk)}
    return render(request, 'projects/detail.html', context)
