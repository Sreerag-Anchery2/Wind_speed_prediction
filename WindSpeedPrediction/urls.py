from django.urls import path
from .views import *


urlpatterns = [
    path("",Landingpage),
    path("prediction",Prediction),
]