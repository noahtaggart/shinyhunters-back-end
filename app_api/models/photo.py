from django.db import models

class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
    trainer = models.ForeignKey("Trainer", on_delete=models.CASCADE)