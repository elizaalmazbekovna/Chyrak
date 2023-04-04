from django.db import models
from datetime import datetime

class Victim(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    place_of_birth = models.CharField(max_length=30)
    place_of_death = models.CharField(max_length=30)
    blame = models.TextField()
    rehabilitated = models.BooleanField()
    occupation = models.CharField(max_length=30)
    bedfellow = models.CharField(max_length=30)
    children = models.CharField(max_length=30)
    photo = models.CharField(max_length=50)
    content = models.TextField(default="0")
    date_of_publish = models.DateField(default=datetime.now)
    up_vote = models.IntegerField(default=0)
    is_proven = models.BooleanField(default=False)
    before_edit_content = models.TextField(default="0")
    after_edit_content = models.TextField(default="0")
    date_of_editing = models.DateField(default=datetime.now)
    def __str__(self):
        return self.first_name + " " + self.last_name

# class Article(models.Model):
#     # victim_id = models.ForeignKey(Victim, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30, default="0")
#     content = models.TextField(default="0")
#     date_of_publish = models.DateField(default=datetime.now)
#     up_vote = models.IntegerField(default=0)
#     is_proven = models.BooleanField(default=False)
#     before_edit_content = models.TextField(default="0")
#     after_edit_content = models.TextField(default="0")
#     date_of_editing = models.DateField(default=datetime.now)
#
#     def __str__(self):
#         return self.title
    # victim_id = models.OneToOneField(Victim, on_delete=models.CASCADE, primary_key=True)