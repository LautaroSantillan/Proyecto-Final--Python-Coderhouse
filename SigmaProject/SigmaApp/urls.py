from django.urls import path
from SigmaApp.views import *

urlpatterns = [
    path('index/', index, name="Home"),
]
