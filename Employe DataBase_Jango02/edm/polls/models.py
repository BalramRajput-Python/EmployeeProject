from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):

 question = models.TextField(max_length=100)
 ch1 = models.CharField(max_length=20)
 ch2 = models.CharField(max_length=20)
 ch3 = models.CharField(max_length=20)
 ans = models.CharField(max_length=20)
 created_by = models.ForeignKey(User,on_delete=models.CASCADE)