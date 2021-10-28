from django.db import models
from django.contrib.auth.models import User


class RoomModel(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
