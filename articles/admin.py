from django.contrib import admin

# Register your models here.
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ("title", "pubdate", "published", "created_by_ai")
    search_fields = ["title"]
    list_filter = (["pubdate", "published", "created_by_ai"])


admin.site.register(Article, ArticleAdmin)