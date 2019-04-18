from django.conf.urls import url, include
from rest_framework import routers
from people.views import PersonViewSet

people_router = routers.DefaultRouter()
people_router.register(r'people', PersonViewSet)

urlpatterns = [
    url(r'^', include(people_router.urls)),
]
