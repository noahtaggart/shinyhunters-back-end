from django.db import models
from django.contrib.auth.models import User
from requests import Response

from app_api.models.following import Following


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=180)

    @property
    def recent_completed_hunt(self):
        recent_hunt = self.hunts.filter(completed=True).last()
        return recent_hunt

    @property
    def is_subscribed(self):
        return self.__is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, value):
        subscribed = Following.objects.filter(trainer=self, follower=value.id)
        if len(subscribed) > 0:
            self.__is_subscribed = True
        else:
            self.__is_subscribed = False
