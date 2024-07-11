from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='mainpage'),
    path('Products/',views.Products,name='Products'),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('UserLogout/',views.UserLogout,name="UserLogout"),
    path('UserProfile/',views.UserProfile,name="UserProfile"),
    path('CateProducts/<int:id>/',views.CateProducts,name="CateProducts"),
    path('CheckoutView/',views.CheckoutView,name="Checkout"),
    path('UserRegisterView/',views.UserRegisterView,name="UserRegisterView"),
    path('PaymentPage/',views.PaymentPage,name="PaymentPage"),
    path('About/',views.About, name='About'),
    path('Contact/',views.Contact, name='Contact'),
    path('Gallery/',views.Gallery, name='Gallery'),
    path('galleryitem', views.galleryitem, name='galleryitem'),
    
]
