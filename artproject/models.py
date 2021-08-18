from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.db import models

# Create your models here.
class Clan(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(
        default="", max_length=350, blank=True, null=True)

    def __str__(self):
        return self.name

class Player(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    clan = models.ForeignKey(Clan, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, unique=True)
    coins = models.IntegerField(default=0, blank=True, null=True)
    max_points = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.username