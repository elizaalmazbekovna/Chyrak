from django.db import models
from datetime import datetime

from Profile.models import Profile


class Victim(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    place_of_birth = models.CharField(max_length=30)
    place_of_death = models.CharField(max_length=30)
    nationality = models.TextField(default='', blank=True, null=True)
    blame = models.TextField(blank=True, null=True)
    rehabilitated = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    bedfellow = models.CharField(max_length=30, blank=True, null=True)
    children = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    desc_of_photo = models.TextField(default='', blank=True, null=True)
    desc_of_file = models.TextField(default='', blank=True, null=True)
    content = models.TextField(default="", blank=True, null=True)
    date_of_publish = models.DateField(default=datetime.now)
    up_vote = models.IntegerField(default=0)
    is_proven = models.BooleanField(default=False)
    before_edit_content = models.TextField(default="")
    after_edit_content = models.TextField(default="")
    date_of_editing = models.DateField(default=datetime.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    x = models.CharField(max_length=100,default="", blank=True, null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name
