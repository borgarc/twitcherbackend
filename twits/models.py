from django.db import models


class Twit(models.Model):
    content = models.CharField(max_length=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='twits')
    retwits = models.ManyToManyField(Person)
    likes = models.ManyToManyField(Person)
    replies = models.ManyToManyField(Person)

class Replies(models.Model):
    content = models.CharField(max_legth=240)
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='replies')
    twit = models.ForeignKey(Twit, on_delete = models.CASCADE, related_name='replies')
    
class Likes(models.Model):
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='likes')
    twit = models.ForeignKey(Twit, on_delete = models.CASCADE, related_name='likes')

class Retitws(models.Model):
    user = models.ForeignKey(Person, on_delete = models.CASCADE, related_name='retwits')
    twit = models.ForeignKey(Twit, on_delete = models.CASCADE, related_name='retwits')
