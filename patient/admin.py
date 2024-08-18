from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobail_no','image']
    
    def first_name(self,object):
        return object.user.first_name
    def last_name(self,object):
        return object.user.last_name
    
    
admin.site.register(Patient,PatientAdmin)
