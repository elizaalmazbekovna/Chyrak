from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone

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
    occupation = models.TextField( blank=True, null=True)
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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + " " + self.last_name

class EditingHistory(models.Model):
        victim = models.ForeignKey(Victim, on_delete=models.CASCADE)
        edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
        date_of_editing = models.DateField(default=timezone.now)
        letters_edited = models.IntegerField(default=0)
        before_edit_content = models.TextField(default="")
        after_edit_content = models.TextField(default="")

        def letters_edited(self):
            return calculate_letters_edited(self.before_edit_content, self.after_edit_content)

        def save(self, *args, **kwargs):
            self.letters_edited = calculate_letters_edited(self.before_edit_content, self.after_edit_content)
            super().save(*args, **kwargs)


def calculate_letters_edited(before_content, after_content):
    """
    Calculates the number of letters edited between the before and after content.
    """
    return abs(len(after_content) - len(before_content))


