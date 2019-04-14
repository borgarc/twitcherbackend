from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from twits.models import Twit, Replies
from twits.serializers import TwitSerializer, RepliesSerializer

class TwitsViewSet(ModelViewSet):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer

class RepliesViewSet(ModelViewSet):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer

