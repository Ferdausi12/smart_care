from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router 
router.register('service', views.ServiceViewsets,) # router of antena

urlpatterns = [
    path('', include(router.urls)),
]