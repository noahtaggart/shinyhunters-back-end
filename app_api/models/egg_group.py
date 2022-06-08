from django.db import models
from .pokemon import Pokemon

class EggGroup(models.Model):
    name = models.CharField(max_length=50)