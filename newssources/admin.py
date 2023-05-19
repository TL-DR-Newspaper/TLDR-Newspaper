from django.contrib import admin

# Register your models here.
from newssources.models import Source

class SourceAdmin(admin.ModelAdmin):
    list_display = ("title", 'use_in_ai', "author")
    list_filter = ('publishedAt', 'use_in_ai', "sourcename", "author",)
    search_fields = ["title"]

admin.site.register(Source, SourceAdmin)