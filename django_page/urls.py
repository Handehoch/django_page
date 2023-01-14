from django.contrib import admin
from django.urls import path, include

from django_page.views import *

urlpatterns = [
    path('', index),
    path('demand', demand),
    path('geography', geography),
    path('skills', skills),
    path('vacancies', vacancies),
    path('admin/', admin.site.urls),
]
