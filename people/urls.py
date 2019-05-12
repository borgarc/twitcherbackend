from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from people.views import PersonViewSet, ProfileView

people_router = routers.DefaultRouter()
people_router.register(r'people', PersonViewSet, base_name='people')

urlpatterns = [
    path(r'profile/', ProfileView.as_view()),
    url(r'^', include(people_router.urls)),
]
