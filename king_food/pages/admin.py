from django.contrib import admin
from .models import *


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','activate' , 'weight')
    search_fields = ('id','name')
    list_editable=('activate',)
    list_filter = ('activate',)

@admin.register(container_of_five_product )
class Container_of_five_productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','activate' , 'weight')
    search_fields = ('id','name')
    list_editable=('activate',)
    list_filter = ('activate',)



@admin.register(about_company)
class About_companyAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'phone_number1' , 'phone_number2' ,)
    search_fields = ('id','Name')

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'  # Optional: to set the column header in the admin panel

@admin.register(quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('id', )



    admin.site.site_header = 'King Food'
    admin.site.site_title =  'King Food'