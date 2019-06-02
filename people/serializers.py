from django.contrib.auth.models import User
from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'user', 'follows', )

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
        fields = ('id', 'name', 'username', 'follows', 'followers')

class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_name(self, person):
        return u'{first_name} {last_name}'.format(
            first_name=person.user.first_name,
            last_name=person.user.last_name,
        )

    def get_username(self, person):
        return u'@{username}'.format(
            username=person.user.username,
        )

    class Meta:
        model = Person
        fields = ('id', 'name', 'username', 'follows', 'followers')

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
        )
        extra_kwargs = {
            'password': { 'write_only': True },
        }
