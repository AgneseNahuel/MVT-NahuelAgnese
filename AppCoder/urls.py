from django.urls import path
from AppCoder.views import *

urlpatterns=[
    path("familia/", familia),
    path("templateapp/", templateapp),
    path("", inicio),

]