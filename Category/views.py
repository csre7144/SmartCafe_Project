from django.shortcuts import render,redirect
from cart.cart import Cart
from Product.models import Product

# Create your views here.
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

def cart_detail(request):
    total =0.00000
    cart = request.session.get('cart', None)
    values= (list(cart.values()))
    for i in values:
        total+=float(i['price'])*float(i['quantity'])
    return render(request, 'cart_detail.html',{'total':total})

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")

