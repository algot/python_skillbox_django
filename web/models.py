from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    text = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
