from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home')
]