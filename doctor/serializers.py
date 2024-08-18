from rest_framework import serializers
from . import models


class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)  #relation ship thakle only ata use krbo
    designation = serializers.StringRelatedField(many=True)  #relation ship thakle only ata use krbo
    specialization = serializers.StringRelatedField(many=True)  #relation ship thakle only ata use krbo
    available_time = serializers.StringRelatedField(many=True)  #relation ship thakle only ata use krbo
    class Meta:
        model = models.Doctor
        fields = '__all__'
        
class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'
        
class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
        
class ReviewSerializers(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Review
        fields = '__all__'