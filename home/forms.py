from django import forms
from .models import Booking,Contact

class ContactForm(forms.ModelForm):
    class Meta:
         model = Contact
         fields = '__all__'
    

class DateInput(forms.DateInput):
    input_type = 'date'



class BookingForm(forms.ModelForm):
        class Meta:
             model=Booking
             fields='__all__'
             widgets = {
            'Booking_date':DateInput(),
             }
             labels = {
            'p_name' :"Patient Name",
            'p_phone' :"Phone Number",
            'p_email' :"Email Address",
            'doc_name' :"Doctor Name",
            'Booking_date' :"Booking date",

            
             }


  
