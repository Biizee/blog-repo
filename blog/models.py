from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=600)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
