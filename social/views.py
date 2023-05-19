from django.shortcuts import render, redirect
from articles.models import Article
import praw
from django.contrib.auth.decorators import login_required
from core.settings import env
import environ


reddit = praw.Reddit(client_id=env("REDDIT_CLIENT_ID"),
                    client_secret=env("REDDIT_CLIENT_SECRET"),
                    user_agent=env("REDDIT_USER_AGENT"),
                    redirect_uri='localhost:8080',
                    refresh_token=env("REDDIT_REFRESH_TOKEN"))
 

@login_required
def post_to_reddit(request, subreddit, id):
    article = Article.objects.get(id=id)
    baseurl = 'https://tldrnewspaper.com/article/'
    slug = str(article.slug)
    title = article.title
    title = title.strip('\"')
    subreddit = reddit.subreddit(subreddit)
    subreddit.submit(title,url=baseurl+slug)
    return redirect('/')

    
