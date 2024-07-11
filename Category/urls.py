from django.urls import path
from . import views
from cart.cart import Cart


urlpatterns = [
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/item_increment/<int:id>/',
    views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
    views.item_decrement, name='item_decrement'),
    path('cart/item_clear/<int:id>/', 
    views.item_clear, name='item_clear'),
]
