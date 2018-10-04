from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    # include Urls from
    path('',home, name='home'),

]
