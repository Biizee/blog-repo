from django.db import models
from django.utils import timezone

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=600)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def published_recently(self):
            return self.publish_date >= timezone.now() - timezone.delta(days = 7)
