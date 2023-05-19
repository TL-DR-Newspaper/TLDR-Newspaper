from django.db import models


# Create your models here.
class Source(models.Model):
    sourceid = models.CharField(max_length=50, null=True)
    sourcename = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=500, null=True)
    description = models.TextField( null=True)
    url = models.CharField(max_length=500, null=True)
    urltoimage = models.CharField(max_length=500, null=True)
    publishedAt = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    use_in_ai = models.BooleanField(default=True)

    def __str__(self):
        return self.title