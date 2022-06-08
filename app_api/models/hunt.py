from django.db import models
from .trainer import Trainer
from .pokemon import Pokemon
from .game import Game
from .method import Method

class Hunt(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    encounters = models.IntegerField()
    completed = models.BooleanField(default=False)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    shiny_charm = models.BooleanField(default=False)