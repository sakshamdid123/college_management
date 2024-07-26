# routing.py
from django.urls import re_path
from .consumers import VettingDataConsumer

websocket_urlpatterns = [
    re_path(r'ws/vetting_data/$', VettingDataConsumer.as_asgi()),
]
