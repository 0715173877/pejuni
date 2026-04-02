from django.shortcuts import render
from services.models import Service
from projects.models import Project
from team.models import TeamMember
from news.models import Article
from core.models import Partner, Testimonial, Statistic, Advantage, HeroContent

def home(request):
    context = {
        'services': Service.objects.all(),
        'projects': Project.objects.order_by('-created_at')[:6],
        'team_members': TeamMember.objects.all(),
        'articles': Article.objects.all(),
        'partners': Partner.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'statistics': Statistic.objects.all(),
        'advantages': Advantage.objects.all(),
        'hero': HeroContent.objects.first(),
        'location_tags': [cat for cat in Project.objects.order_by().values_list('country', flat=True).distinct() if cat][:6],
    }
    return render(request, 'index.html', context)

def company_view(request):
    return render(request, 'core/company.html')

def community_view(request):
    return render(request, 'core/community.html')

def partners_view(request):
    context = {'partners': Partner.objects.all()}
    return render(request, 'core/partners.html', context)
