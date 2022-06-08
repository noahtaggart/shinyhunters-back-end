from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    default_sprite = models.CharField(max_length=300, default=None, null=True)
    female_sprite = models.CharField(max_length=300, default=None, null=True)
    egg_groups = models.ManyToManyField("EggGroup", related_name="pokemon")
    shiny_locks = models.ManyToManyField("Game", related_name="lockedpokemon")
    games = models.ManyToManyField("Game", related_name="pokemon")
    
    
    