from django.shortcuts import render
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Partner, Testimonial

def home(request):
    context = {
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'team_members': TeamMember.objects.all(),
        'articles': Article.objects.all(),
        'partners': Partner.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'index.html', context)
