from django.db import models
from accounts.models import CustomUser



class Advertisement(models.Model):
    user = models.ForeignKey(CustomUser, related_name='imageuser', on_delete=models.CASCADE, default=2)
    age = models.IntegerField()
    education = models.CharField(max_length=64)
    experience = models.IntegerField()
    details = models.TextField()
    pub_date = models.DateTimeField('date published')

