from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class ServiceViewsets(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializers
