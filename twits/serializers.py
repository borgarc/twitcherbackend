from rest_framework import serializers
from twits.models import Twit, Replies

class TwitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twit
        fields = ('id', 'user', 'content', 'retwited_by', 'liked_by', )

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ('id', 'content', 'user', 'twit', )

