from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from twits.models import Twit, Reply
from twits.serializers import TwitSerializer, TwitSaveSerializer, RepliesSerializer

class TwitsViewSet(ModelViewSet):
    queryset = Twit.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created')
    ordering = ('-created',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TwitSaveSerializer
        return TwitSerializer


class RepliesViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = RepliesSerializer
