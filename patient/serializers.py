from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework import serializers



class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
        
# class RegistrationSerializer(serializers.ModelSerializer):
#     password_confirm = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username','first_name', 'last_name', 'email', 'password', 'password_confirm']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value

#     def validate(self, data):
#         if data['password'] != data['password_confirm']:
#             raise serializers.ValidationError("Passwords do not match.")
#         return data

#     def create(self, validated_data):
#         validated_data.pop('password_confirm')
#         user = User.objects.create_user(**validated_data)
#         return user

        
# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required = True)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        
#     def save(self):
#         username = self.validated_data['username']
#         email = self.validated_data['email']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         password = self.validated_data['password']
#         password2 = self.validated_data['confirm_password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error': "password doesn't match"})
        
#         if User.objects.filter(email= email).exists:
#             raise serializers.ValidationError({'error': "email already exist"})
        
#         account = User(username = username,email=email,first_name = first_name,last_name=last_name)
#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account

# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required = True)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
#     def save(self):
#         username = self.validated_data['username']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         password2 = self.validated_data['confirm_password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'error' : "Email Already exists"})
#         account = User(username = username, email=email, first_name = first_name, last_name = last_name)
#         print(account)
#         account.set_password(password)
#         account.is_active = False
#         account.save()
#         return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    


    