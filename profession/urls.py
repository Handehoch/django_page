from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('demand', demand),
    path('geography', geography)
]
