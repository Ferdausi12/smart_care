from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appointment_types','appointment_status','symptoms','time','cancle']
    def patient_name(self,object):
        return object.patient.user.first_name
    def doctor_name(self,object):
        return object.doctor.user.first_name
    
    def save_model(self,request,obj,form,change):
        
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            
        # obj.save()
        # if obj.appointment_status == "Running" and obj.appointment_types == "online":
        #     email_subject = "Your Online Poointment is Runnig"
        #     email_body = render_to_string('admin_email.html', {'user': obj.patient.user, 'doctor':obj.doctor})
        #     email = EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
        #     email.attach_alternative(email_body, 'text/html')
        #     email.send()
            
    
admin.site.register(models.Appointment,AppointmentAdmin)
