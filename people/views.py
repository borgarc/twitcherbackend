from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from people.filters import PersonFilter
from people.models import Person
from people.serializers import PersonSerializer, ProfileSerializer, PersonTwitSerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PersonFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return PersonSerializer
        return PersonTwitSerializer

class ProfileView(GenericAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, format=None):
        person = Person.objects.get(user=request.user)
        serializer = ProfileSerializer(person)
        return Response(serializer.data)

