from django.db import models


class EggGroup(models.Model):
    name = models.CharField(max_length=50)