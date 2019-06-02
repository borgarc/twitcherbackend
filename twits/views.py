from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from people.models import Person
from twits.models import Twit, Reply
from twits.serializers import TwitSerializer, TwitSaveSerializer, RepliesSerializer, RepliesSaveSerializer

class TwitsViewSet(ModelViewSet):
    filter_backends = (OrderingFilter,)
    ordering_fields = ('created')
    ordering = ('-created',)

    def get_queryset(self):
        user = self.request.query_params['user']
        my_twits = Q(user=user)
        following_twits = Q(user__followers=user)
        return Twit.objects.filter(my_twits | following_twits).distinct()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TwitSaveSerializer
        return TwitSerializer


class RepliesViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend,)
    ordering_fields = ('created')
    ordering = ('-created',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RepliesSaveSerializer
        return RepliesSerializer

