from django.shortcuts import render
from django.db.models import Prefetch
from articles.models import Article, ArticleTag

def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at').prefetch_related(
        Prefetch('scopes', queryset=ArticleTag.objects.select_related('tag').order_by('-is_main', 'tag'))
        )
    context = {
        'object_list': articles,
    }

    return render(request, template, context)
 