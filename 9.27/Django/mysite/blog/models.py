from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    content = models.TextField('内容')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name