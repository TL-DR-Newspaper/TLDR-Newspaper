from django.shortcuts import render, redirect
from .models import Article
from newssources.models import Source
from django.contrib.auth.decorators import login_required



# Create your views here.
def article_by_slug(request, slug):
    article = Article.objects.filter(slug=slug).last()
    sources = article.sources.all()
    context = {'article':article, 'sources':sources}
    return render(request, "article_index.html", context)

def article_by_id(request, id):
    article = Article.objects.get(id=id)
    sources = article.sources.all()
    context = {'article':article, 'sources':sources}
    return render(request, "article_index.html", context)


@login_required
def unpublish_article(request, slug):
    article = Article.objects.filter(slug=slug).last()
    article.published = False
    article.save()
    return redirect('/')

@login_required
def edit_article(request, slug):
    article = Article.objects.filter(slug=slug).last()
    return redirect('http://localhost:8000/admin/articles/article/'+str(article.id)+'/change/')

@login_required
def next_article(request, slug):
    article = Article.objects.filter(slug=slug).last()
    i = 1
    found = Article.objects.filter(pk=article.id + i).exists()
    if found:
        new_article = Article.objects.get(pk=article.id + i)
        return redirect('/'+new_article.slug)
    else:
        return redirect('/')