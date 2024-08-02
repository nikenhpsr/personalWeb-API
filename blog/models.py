from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
class BlogMedia(models.Model):
    blog = models.ForeignKey(Blog, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='blog_media/')
