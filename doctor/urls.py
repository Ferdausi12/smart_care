from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # router 
router.register('doctor', views.DoctorViewsets,) 
router.register('specialization', views.SpecializationViewsets,) 
router.register('designation', views.DesignationViewsets,) 
router.register('availabletime', views.AvailableTimeViewsets,) 
router.register('review', views.ReviewViewsets,) 

urlpatterns = [
    path('', include(router.urls)),
]