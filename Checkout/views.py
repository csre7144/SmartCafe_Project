from django.shortcuts import render,redirect
from .forms import CheckOutForm
from .models import Checkout
import datetime
from time import gmtime, strftime


# Create your views here.

def CheckOutView(request):
    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        price = request.POST['price']
        qty = request.POST['qty']
        total = request.POST['total']
        username = request.POST['username']
        code = request.POST['cod']
        data = Checkout(name=name,last_name=last_name,address=address,phone_number=phone_number,price=price,qty=qty,total=total,username=username,code=code)
        if data:
            data.save()
            data1 = datetime.datetime.now()
            return render(request,"invoice.html",{'data':data,'data1':data1})

            # return redirect('invoice')
    return render(request,"checkout.html")


def invoice(request):

    return render(request,"invoice.html")