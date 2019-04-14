from rest_framework import serializers
from twits.models import Twit

class TwitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twit
        fields = ('id', 'content', )

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ('content', )
