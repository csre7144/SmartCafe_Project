from django.urls import path
from . import views

urlpatterns = [
    path('',views.CheckOutView,name="CheckOutView"),
    path('invoice/',views.invoice,name="invoice")
] 