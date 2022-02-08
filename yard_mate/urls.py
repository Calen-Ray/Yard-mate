
# Auto generated by Django helper
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import *




app_name = 'yard_mate'
router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')


urlpatterns = router.urls + [
    path('test/', test),
    path('makes/', makes),
    path('models/', models),
    path('results/<int:make>/<int:model>/<int:distance>/<int:zip>/', results),
]

