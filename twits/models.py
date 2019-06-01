from django.db import models
from people.models import Person
from twitcherbackend.models import BaseModel

class Twit(BaseModel):
    content = models.CharField(max_length=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='twits')
    retwited_by = models.ManyToManyField(Person, related_name='retwits', blank = True)
    liked_by = models.ManyToManyField(Person, related_name='likes', blank = True)

class Reply(BaseModel):
    content = models.CharField(max_length=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='replies')
    twit = models.ForeignKey(Twit, on_delete = models.CASCADE, related_name='replies')

    class Meta:
        verbose_name_plural = 'Replies'
