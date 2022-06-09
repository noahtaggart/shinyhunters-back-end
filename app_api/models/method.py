from django.db import models
from fractions import Fraction


class Method(models.Model):
    name = models.CharField(max_length=50)
    default_odds = models.DecimalField(max_digits=10, decimal_places=10)
    shiny_charm_odds = models.DecimalField(max_digits=10, decimal_places=10)
    games = models.ManyToManyField("Game", related_name="method")
    
    @property
    def default_odds_fraction(self):
        
        return str(Fraction(self.default_odds).limit_denominator(max_denominator=4096))
    
    @property
    def shiny_charm_odds_fraction(self):
        return str(Fraction(self.shiny_charm_odds).limit_denominator(max_denominator=4096))
        
        