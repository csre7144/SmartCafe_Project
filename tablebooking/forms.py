from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bookingDate"].widget.attrs.update({"class": "my-calendar bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["booking_name"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["booking_time"].widget.attrs.update({"class": "selection-1"})
        self.fields["booking_phone"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["person"].widget.attrs.update({"class": "selection-1"})
        self.fields["booking_email"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        
        