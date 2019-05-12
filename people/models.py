from django.contrib.auth.models import User
from django.db import models
from twitcherbackend.models import BaseModel

class Person(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='person')
    followers = models.ManyToManyField('self', related_name='following', blank = True)
