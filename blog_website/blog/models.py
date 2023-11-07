from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from .constants import STATUS_OF_POST_CHOICES, DRAFT


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    status_of_post = models.CharField(choices=STATUS_OF_POST_CHOICES, default=DRAFT, max_length=50)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
