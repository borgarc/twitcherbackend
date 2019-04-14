from django.db import models
from people.models import Person


class Twit(models.Model):
    content = models.CharField(max_length=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='twits')
    retwited_by = models.ManyToManyField(Person, related_name='retwits')
    liked_by = models.ManyToManyField(Person, related_name='likes')

class Replies(models.Model):
    content = models.CharField(max_length=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='replies')
    twit = models.ForeignKey(Twit, on_delete = models.CASCADE, related_name='replies')
