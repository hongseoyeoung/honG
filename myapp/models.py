from django.db import models

class Lecture_note(models.Model):
    title = models.CharField(max_length=200)
    