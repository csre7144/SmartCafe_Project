from django.shortcuts import render,redirect
from Category.models import Category
from .models import  Product
from Checkout.forms import CheckOutForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegister,UserProfileForms
from tablebooking.forms import TableBookingForm
from Checkout.models import Checkout

# Create your views here.

def index(request):
    data = Category.objects.filter(status=True)
    forms = TableBookingForm(request.POST)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect('mainpage')
    context = {
        'data':data,
        'form':forms,
    }
    return render(request,'index.html',context)


def Products(request):
    data = Product.objects.all()
    return render(request,"products.html",{'data':data})

def UserLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('mainpage')
        else:
            return render(request,"SignUp.html",{'msg':"Invalid Username Or Password"})
    return render(request,"SignUp.html")


def UserRegisterView(request):
    data = UserRegister(request.POST)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('UserLogin')
        else:
            print("Error")
    return render(request,"Register.html",{'data':data})





def UserProfile(request):
    data = UserProfileForms(request.POST or None,instance=request.user)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('mainpage')
        else:
            print('Error')
    return render(request,"profile.html",{'data':data})

def UserLogout(request):
    logout(request)
    return redirect('mainpage')



def CateProducts(request,id):
    data = data = Product.objects.filter(category=id)
    return render(request,"ProductCate.html",{'data':data})

def PaymentPage(request):
    return render(request,"payment.html")

def CheckoutView(request):
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
            return redirect('PaymentPage')
    return render(request,"checkout.html")

def About(request):
    return render(request,"about.html")

def Contact(request):
    return render(request, "contact.html")

def Gallery(request):
    return render(request,"gallery.html")

def galleryitem(request):
    return render(request, "galleryitem.html")


