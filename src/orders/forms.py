from django import forms

from .models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer_first_name',
            'customer_last_name',
            'customer_email',
            'customer_tel',
        ]
