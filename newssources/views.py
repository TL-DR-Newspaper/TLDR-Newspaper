from django.shortcuts import render, HttpResponse
import requests
from .models import Source
from core.settings import NEWS_API_KEY
from django.contrib.auth.decorators import login_required


def save_news(url):
    #Fetching headlines
    r = requests.get(url)
    response = r.json()
    print(response['numResults'], ' articles found')
    for article in response['articles']:
        if Source.objects.filter(url = article['url']):
            pass
        else:
            newsource = Source(sourceid = article['articleId'], 
                            sourcename = article['source']['domain'],
                            author = article['authorsByline'],
                            title = article['title'],
                            description = article['description'],
                            urltoimage = article['imageUrl'],
                            url = article['url'],
                            publishedAt = article['pubDate'],
                            content = article['content']
                            )
            newsource.save()

@login_required
def get_news(request):
    #APIKEY = NEWS_API_KEY
    i = 1
    go = True
    while go:
        goperigon = 'https://api.goperigon.com/v1/all?apiKey='+NEWS_API_KEY+'&from=2023-05-16&to=2023-05-17&language=en&sourceGroup=top10&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=PaidNews&excludeLabel=Roundup&excludeLabel=PressRelease&sortBy=date&page='+str(i)
        print(i)
        save_news(goperigon)
        i = i+1
        if i == 100:
            go == False

    return HttpResponse(204)
