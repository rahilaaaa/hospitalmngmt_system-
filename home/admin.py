from django.contrib import admin
from .models import Departments,Doctor,Booking,Contact
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','doc_name','Booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','messege')
admin.site.register(Contact,ContactAdmin)



