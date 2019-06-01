from rest_framework import serializers
from twits.models import Twit, Reply
from people.serializers import PersonTwitSerializer

class TwitSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twit
        fields = ('id', 'user', 'content', 'retwited_by', 'liked_by', 'created',)

class TwitSerializer(serializers.ModelSerializer):
    user = PersonTwitSerializer(read_only=True)
    
    class Meta:
        model = Twit
        fields = ('id', 'user', 'content', 'retwited_by', 'liked_by', 'created',)

class RepliesSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'content', 'user', 'twit', 'created')

class RepliesSerializer(serializers.ModelSerializer):
    user = PersonTwitSerializer(read_only=True)
    class Meta:
        model = Reply
        fields = ('id', 'content', 'user', 'twit', 'created')

