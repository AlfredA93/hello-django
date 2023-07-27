"Libraries"
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    "Form"
    class Meta:
        "Info about the form fields"
        model = Item
        fields = ['name', 'done']
