from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'news/list.html', context)

def article_detail(request, pk):
    context = {'article': get_object_or_404(Article, pk=pk)}
    return render(request, 'news/detail.html', context)
