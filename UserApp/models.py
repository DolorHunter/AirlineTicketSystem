from django.db import models


class UserItem(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
