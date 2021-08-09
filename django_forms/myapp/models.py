from django.db import models

class Snippet(models.Model):
    word = models.TextField()

    def __str__(self) -> str:
        return self.word