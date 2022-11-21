from django.urls import path
from AppCoder.views import *

urlpatterns=[
    path("familia/", familia, name="familia"),
    path("templateapp/", templateapp, name="templateapp"),
    path("", inicio, name="inicio"),
    path("familia2/", familiaprueba, name="familiaprueba"),
]