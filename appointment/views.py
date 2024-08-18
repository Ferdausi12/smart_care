from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class AppointmentViewsets(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializers
    
    # custom queryset krtesi id diye khujar jnno
    def get_queryset(self):
        queryset = super().get_queryset()  #inherit krlam all queryset ta(/?patient_id=1)
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset
    
    def get_queryset(self):
        queryset = super().get_queryset()  #inherit krlam all queryset ta(/?patient_id=1)
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(doctor_id = doctor_id)
        return queryset
    
