from django.db import models
from django.utils import timezone
from django.contrib import admin



class Flashcard(models.Model):
    front_text = models.CharField(max_length=100)
    back_text = models.CharField(max_length=100)


class CollectionOfFlashCards(models.Model):
    flashcards = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    
    pub_date = models.DateTimeField("date published")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
