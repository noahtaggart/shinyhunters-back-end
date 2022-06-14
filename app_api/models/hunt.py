from datetime import date
from django.db import models


class Hunt(models.Model):
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE, related_name='hunts')
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE)
    encounters = models.IntegerField()
    completed = models.BooleanField(default=False)
    method = models.ForeignKey('Method', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    shiny_charm = models.BooleanField(default=False)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)