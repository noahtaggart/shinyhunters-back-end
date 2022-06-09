from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Method(models.Model):
    name = models.CharField(max_length=50)
    default_odds = models.DecimalField(max_digits=100, decimal_places=100)
    shiny_charm_odds = models.DecimalField(max_digits=100, decimal_places=100)
    games = models.ManyToManyField("Game", related_name="method")