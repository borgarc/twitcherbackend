from django.conf.urls import url, include
from rest_framework import routers
from twits.views import TwitsViewSet

twits_router = routers.DefaultRouter()
twits_router.register(r'twits', TwitsViewSet)

urlpatterns = [
    url(r'^', include(twits_router.urls)),
]
