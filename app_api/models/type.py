from django.db import models


class Type(models.Model): 
    label = models.CharField(max_length=50)
    pokemon = models.ManyToManyField('Pokemon', related_name="types")