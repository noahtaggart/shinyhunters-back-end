from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Method(models.Model):
    name = models.CharField(max_length=50)
    default_odds = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    shiny_charm_odds = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    games = models.ManyToManyField("Game", related_name="method")