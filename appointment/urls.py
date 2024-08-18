from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router or wifi create krlam
router.register('appointment', views.AppointmentViewsets,) # router of antena

urlpatterns = [
    path('', include(router.urls)),
]