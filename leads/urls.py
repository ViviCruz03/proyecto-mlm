from django.urls import path, reverse
from .views import *

urlpatterns = [
    path('', home, name='index'),
]