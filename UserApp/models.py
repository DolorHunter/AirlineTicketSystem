from django.db import models


class UserAppItem(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
