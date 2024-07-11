from django import forms
from .models import Checkout


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["last_name"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["address"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        self.fields["phone_number"].widget.attrs.update({"class": "bo-rad-10 sizefull txt10 p-l-20"})
        