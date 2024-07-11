from django.db import models

# Create your models here.
class TableBooking(models.Model):
    bookingDate = models.CharField(max_length=200)
    booking_name = models.CharField(max_length=30)
    booking_time = models.CharField(max_length=30,choices=(
        ("10:00 am","10:00 am"),
        ("10:30 am","10:30 am"),
        ("11:00 am","11:00 am"),
        ("11:45 am","11:45 am"),
        ("12:30 pm","12:30 pm"),
        ("1:30 pm","1:30 pm"),
        ("2:30 pm","2:30 pm"),
        ("3:00 pm","3:00 pm")
    ))
    # booking_phone = models.IntegerField(max_length=10)
    booking_phone = models.CharField(max_length=10)
    person = models.CharField(max_length=2,choices=(
        ('1',"1"),
        ('2',"2"),
        ('3',"3"),
        ('4',"4"),
        ('5',"5"),
        ('6',"6"),
        ('7',"7"),
        ('8',"8"),
        ('9',"9"),
        ('10',"10"),
        ('11',"11"),
        ('12',"12"),


    ))
    booking_email = models.EmailField()
    