from django.contrib import admin
from  .models import Vendor

# Register your models here.

@admin.register(Vendor)
class Vendoradmin(admin.ModelAdmin):
    list_display = ['vendor_id','name','user', 'vendors_image','mobile','date']

