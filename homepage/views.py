from django.shortcuts import render
from articles.models import Article
from django.db.models import Count
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 3)
def index(request):
    articles = Article.objects.filter(published=True, created_by_ai=True).order_by('-sources')
    #articles = Article.objects.annotate(most_sources=Count("sources")).order_by("most_sources")
    hero = articles[:3]
    highlighted = articles[3:21]
    frontpage = articles[22:36]
    older = articles[36:100]
    context = {'hero':hero, 'highlighted':highlighted, 'frontpage':frontpage, 'older':older}
    return render(request, "homepage.html", context)

@cache_page(60 * 60)
def faq(request):
    context = {}
    return render(request, "faq_index.html", context)

@cache_page(60 * 60)
def funding(request):
    context = {}
    return render(request, "funding_index.html", context)

@cache_page(60 * 60)
def responsibleai(request):
    context = {}
    return render(request, "ai_index.html", context)