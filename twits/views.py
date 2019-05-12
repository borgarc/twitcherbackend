from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from twits.models import Twit, Reply
from twits.serializers import TwitSerializer, RepliesSerializer

class TwitsViewSet(ModelViewSet):
    queryset = Twit.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created')
    ordering = ('-created',)
    serializer_class = TwitSerializer

class RepliesViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = RepliesSerializer
