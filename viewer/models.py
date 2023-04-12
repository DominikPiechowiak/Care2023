from django.db import models
from accounts.models import CustomUser


class Advertisement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = CustomUser.first_name
    last_name = CustomUser.last_name
    email = CustomUser.email
    age = models.IntegerField()
    education = models.CharField(max_length=64)
    experience = models.IntegerField()
    details = models.TextField()
    pub_date = models.DateTimeField('date published')

