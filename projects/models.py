from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    tech_stack = models.JSONField(default=list)
    description = models.TextField()
    link = models.JSONField(default=list)

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50)
    media_link = models.URLField()