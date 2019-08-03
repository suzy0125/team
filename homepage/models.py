from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    component = models.TextField(null=True)
    published_date = models.DateTimeField(blank=True, null = True)
    photo = models.ImageField(blank=True, null=True)
    
    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post=models.ForeignKey('homepage.Post', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


  