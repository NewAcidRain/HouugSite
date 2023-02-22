from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",startPage),
    path('login/', LoginUser.as_view()),
    path('registration/', RegisterUser.as_view())
]