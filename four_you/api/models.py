from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.JSONField(default=list)  # Store cart items as a list of dictionaries

    def __str__(self):
        return f"{self.user.username}'s Cart"