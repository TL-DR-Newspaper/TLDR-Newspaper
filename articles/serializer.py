from .models import Article
from newssources.models import Source
from rest_framework import serializers

class sourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    sources = sourceSerializer(read_only=True, many=True)
    
    class Meta:
        model = Article
        fields = ['title', 'imageurl', 'pubdate', 'summary',  'comparison', 'long_content', 'views', 'sources',]