from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from twitcherbackend.models import BaseModel

class Person(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='person')
    follows = models.ManyToManyField('self', related_name='followers', blank = True, symmetrical=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
