from django.shortcuts import render, HttpResponse
import requests
from .models import Source
from core.settings import NEWS_API_KEY
from django.contrib.auth.decorators import login_required


def save_news(url):
    #Fetching headlines
    r = requests.get(url)
    response = r.json()
    if response["status"] != "ok":
        print(response["message"])
    else:
        for article in response['articles']:
            if Source.objects.filter(url = article['url']):
                pass
            else:
                newsource = Source(sourceid = article['source']['id'],
                                sourcename = article['source']['name'],
                                author = article['author'],
                                title = article['title'],
                                description = article['description'],
                                urltoimage = article['urlToImage'],
                                url = article['url'],
                                publishedAt = article['publishedAt'],
                                content = article['content']
                                )
                newsource.save()

@login_required
def get_news(request):
    i = 1
    go = True
    while go:
        url =  'https://newsapi.org/v2/top-headlines?country=us&pageSize=99&page='+str(i)+'&apiKey='+NEWS_API_KEY
        #url = 'https://api.goperigon.com/v1/all?apiKey='+NEWS_API_KEY+'&from=2023-05-16&to=2023-05-17&language=en&sourceGroup=top10&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=PaidNews&excludeLabel=Roundup&excludeLabel=PressRelease&sortBy=date&page='+str(i)
        print(i)
        save_news(url)
        i = i+1
        if i == 5:
            go == False

    return HttpResponse(204)
