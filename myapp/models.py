from django.db import models

class Lecture_note(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=200)
    