from django.db import models


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
    def __str__(self):
        return self.first_name + " " + self.last_name

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_of_publish = models.DateField()
    up_vote = models.IntegerField()
    is_proven = models.BooleanField()
    before_edit_content = models.TextField()
    after_edit_content = models.TextField()
    date_of_editing = models.DateField()

    def __str__(self):
        return self.title
    # victim_id = models.OneToOneField(Victim, on_delete=models.CASCADE, primary_key=True)