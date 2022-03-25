from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models

class Verbs(models.Model):
    verb = models.CharField(blank=True, max_length=20, default='fart')

    def __str__(self):
        return self.verb
