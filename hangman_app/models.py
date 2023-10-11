from django.db import models

class HangmanGame(models.Model):
    word = models.CharField(max_length=100)
    guessed_letters = models.CharField(max_length=100, default='')
    incorrect_guesses = models.IntegerField(default=0)
    max_incorrect_guesses = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='InProgress')

    def __str__(self):
        return self.word
