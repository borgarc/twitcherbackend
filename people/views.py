from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from people.models import Person
from people.serializers import PersonSerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

