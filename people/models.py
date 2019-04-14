from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='person')
    followers = models.ManyToManyField('self', related_name='following')

