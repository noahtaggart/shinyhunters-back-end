from django.db import models
from django.contrib.auth.models import User
from requests import Response

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=180)
    
    @property
    def recent_completed_hunt(self):
        recent_hunt = self.hunts.filter(completed = True).last()
        return recent_hunt