from django import forms
from django.db import models
from django.db.models import fields
from .models import Order


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        # fields = ['customer_id', 'product_id', 'quantity', 'delivary']