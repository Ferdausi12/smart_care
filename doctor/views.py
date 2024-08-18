from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 

# Create your views here.
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100
    
    
class DoctorViewsets(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializers
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
class SpecializationViewsets(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializers
    

    
class DesignationViewsets(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DoctorSerializers
    
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
    
class AvailableTimeViewsets(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]
    
class ReviewViewsets(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializers
