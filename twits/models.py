from django.db import models


class Twit(models.Model):
    content = models.CharField(max_length=240)

