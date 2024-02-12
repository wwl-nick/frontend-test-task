from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=225, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apps')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='apps')
    icon = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
