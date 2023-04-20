from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Post(models.Model):
    education = models.CharField(max_length=64)
    experience = models.TextField(max_length=600)
    details = models.TextField(max_length=600)
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, related_name='imageuser', on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
