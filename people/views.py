from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from people.models import Person
from people.serializers import PersonSerializer, ProfileSerializer, PersonTwitSerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonTwitViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonTwitSerializer

class ProfileView(GenericAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        person = Person.objects.get(user=request.user)
        serializer = ProfileSerializer(person)
        return Response(serializer.data)

