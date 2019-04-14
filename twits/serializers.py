from rest_framework import serializers
from twits.models import Twit, Reply

class TwitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twit
        fields = ('id', 'user', 'content', 'retwited_by', 'liked_by', )

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'content', 'user', 'twit', )

