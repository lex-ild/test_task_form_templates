from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('get_form/', find_form_template, name='find-template')
]