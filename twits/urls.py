from django.conf.urls import url, include
from rest_framework import routers
from twits.views import TwitsViewSet, RepliesViewSet

twits_router = routers.DefaultRouter()
twits_router.register(r'replies', RepliesViewSet, base_name='replies')
twits_router.register(r'twits', TwitsViewSet, base_name='twits')

urlpatterns = [
    url(r'^', include(twits_router.urls)),
]
