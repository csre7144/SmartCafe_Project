from django.contrib import admin
from .models import TableBooking
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Register your models here.


admin.site.register(TableBooking)