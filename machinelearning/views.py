from django.shortcuts import render, HttpResponse
from newssources.models import Source
from articles.models import Article
#from sentence_transformers import SentenceTransformer
from django.contrib.auth.decorators import login_required
#import numpy as np
import openai 
from django.utils.text import Truncator
from core.settings import OPENAI_API


MIN_SIMILARITY = 0.50 # Pick between -1 and + 1 
MAX_SIMILARITY = 0.98 # To filter out duplicates
NUMBER_OF_SOURCES = 10000
PROMPT_TITLE = "this is a list of news headlines. Please summarize them into 1 catchy headline: "
PROMPT_SUMMARY = 'This is a list of newspaper articles about the same topic. Please summarize them into 1 paragraph: '
PROMPT_DIFFERENCES = 'List the key differences between the authors in the list: '
openai.api_key = OPENAI_API

def text_generator(input):
  # create a completion
  text_generator = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": input}
    ]
)
  text_string = text_generator["choices"][0]["message"]['content']
  return text_string

@login_required
def analyse(request):
    #https://huggingface.co/flax-sentence-embeddings/all_datasets_v3_mpnet-base
    sources = Source.objects.filter(use_in_ai=True)[:NUMBER_OF_SOURCES] #Getting a subset
    titles = [] #Getting the titles in sentences
    for source in sources:
        titles.append(source.title)
    #model = SentenceTransformer('sentence-transformers/all-mpnet-base-v1')
    embeddings = model.encode(titles)
    print("Analysing all strings")
    i = 0 #To keep track of the item we are on
    for source in embeddings: #For each item, we loop over each item 
        j = 0  #To keep track of which item we're comparing to i 
        for source in embeddings: #comparing all entries for j against i. 
            print("Comparing : ", i, 'and', j ) #Keeping track of where we are
            #similarity = np.dot(embeddings[i], embeddings[j], out=None) #Here we compare
            if similarity >= MIN_SIMILARITY and similarity <= MAX_SIMILARITY: #If they are similar
                article1 = sources[i] #then these are the indexes 
                article2 = sources[j]
                if Article.objects.filter(title=sources[i].title).exists(): #if an article already exists
                    existing_article = Article.objects.get(title=article1.title) #get thet article
                    existing_article.sources.add(article2.id)  #and append
                    existing_article.save() #save
                else: #if it does not exist create a new article
                    new_article = Article( 
                        title = sources[i].title.strip('\"'),
                        imageurl = sources[i].urltoimage,
                        summary = sources[i].content,
                        comparison = sources[i].description,             
                    )
                    new_article.save()
                    new_article.sources.add(article1.id)
                    new_article.sources.add(article2.id) #and add the related source
                    new_article.save()
            j = j + 1 #increment j, so we can compare the next source to i
        i = i +1  #If we have compared all sources to i, then we increment i by 1 so we will start comparing again.
    return HttpResponse(204)

@login_required
def create_summaries(request):
    articles = Article.objects.filter(created_by_ai=False).order_by('-sources')[:70] # We only show the first 50 on the homepage
    for article in articles:
        print("Processing article: ", article, " - ", article.id)
        titles = []
        content = []
        for source in article.sources.all():
            titles.append(source.title)
        for source in article.sources.all():
            content.append({'author': source.sourcename, 'content': source.description})
        generated_title = text_generator(PROMPT_TITLE + str(titles))
        generated_summary = text_generator(PROMPT_SUMMARY + str(content))
        generated_differences = text_generator(PROMPT_DIFFERENCES + str(content))
        #generated_title = "HI I AM PETER"
        #generated_summary = 'I AM THE SUMMARY'
        #generated_differences = 'PETER IS DIFFERENT FROM SUMMARY'
        print(article.id)
        article.title = generated_title
        article.summary = generated_summary
        article.comparison = generated_differences
        article.created_by_ai = True
        article.published = True
        article.save()
    return HttpResponse(204)



