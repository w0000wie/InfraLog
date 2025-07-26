from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True, default="")

    def __str__(self):
        return f"Perfil de {self.user.username}"
from django.apps import AppConfig