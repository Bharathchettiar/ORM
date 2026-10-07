from django.db import models
from django.contrib import admin
class vehicles_DB(models.Model):
    reg_no=models.TextField()
    vehicle_model_name=models.CharField(max_length=32)
    owner_name=models.CharField(max_length=32)
    owner_Email=models.EmailField()
    owner_contact_no=models.IntegerField()
    owner_Address=models.TextField()
    dl_no=models.IntegerField(primary_key=True)
    
class vehicles_DBAdmin(admin.ModelAdmin):
    list_display=["reg_no","owner_name","vehicle_model_name","owner_contact_no","dl_no","owner_Email","owner_Address"]