from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

class Advertisement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = CustomUser.first_name
    last_name = CustomUser.last_name
    email = CustomUser.email
    age = models.IntegerField()
    wykształcenie = models.CharField(max_length=64)
    experience = models.IntegerField()
    details = models.TextField()
    pub_date = models.DateTimeField('date published')