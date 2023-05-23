
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    work_place=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username