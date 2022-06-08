from django.db import models

class Following(models.Model):
    trainer = models.ForeignKey("Trainer", on_delete=models.CASCADE, related_name="Trainers")
    follower = models.ForeignKey("Trainer", on_delete=models.CASCADE, related_name="Follower")
    created_on = models.DateTimeField(auto_now=True)