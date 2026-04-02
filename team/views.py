from django.shortcuts import render, get_object_or_404
from .models import TeamMember

def team_list(request):
    context = {'team_members': TeamMember.objects.all()}
    return render(request, 'team/list.html', context)

def team_detail(request, pk):
    context = {'member': get_object_or_404(TeamMember, pk=pk)}
    return render(request, 'team/detail.html', context)
