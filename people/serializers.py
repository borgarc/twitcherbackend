from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'user', 'followers', )

class PersonTwitSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_name(self, twit):
        return u'{first_name} {last_name}'.format(
            first_name=twit.user.first_name,
            last_name=twit.user.last_name,
        )
    
    def get_username(self, twit):
        return u'@{username}'.format(
            username=twit.user.username,
        )
    
    class Meta:
        model = Person
        fields = ('id', 'name', 'username',)

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    def get_name(self, person):
        return u'{first_name} {last_name}'.format(
            first_name=person.user.first_name,
            last_name=person.user.last_name,
        )

    def get_username(self, person):
        return u'@{username}'.format(
            username=person.user.username,
        )


    def get_followers(self, person):
        return person.followers.count()

    def get_following(self, person):
        return Person.objects.filter(followers__id=person.id).count()

    class Meta:
        model = Person
        fields = ('id', 'name', 'username', 'followers', 'following')
