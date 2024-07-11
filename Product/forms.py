from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User  


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your First Name"})
        self.fields["last_name"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Last Name"})
        self.fields["email"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Email"})
        self.fields["username"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Username"})
        self.fields["password1"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Password"})
        self.fields["password2"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Confirm Password"})


class UserProfileForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your First Name"})
        self.fields["last_name"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Last Name"})
        self.fields["email"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Email"})
        self.fields["username"].widget.attrs.update({"class": "col-md-12","placeholder":"Enter Your Username"})
       