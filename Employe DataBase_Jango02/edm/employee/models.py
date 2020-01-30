from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):

  user = models.ForeignKey(User,on_delete=models.CASCADE)
  Qualification = models.CharField(max_length=50)
  WorkExp = models.TextField(max_length=200)
  user_type = models.CharField(max_length=50,default="")
  