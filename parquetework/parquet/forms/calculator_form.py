from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField


class CalculatorForm(forms.Form):
    name = forms.CharField(label=_('Имя'), max_length=15)
    phone_number = PhoneNumberField(label='Телефон', widget=forms.TextInput(attrs={
        'placeholder': '+7 (___) ___-__-__',
        'pattern': '\+7\(\d{3}\) \d{3}-\d{2}-\d{2}',
        'id': 'phone-input',
        'oninput': 'formatPhone(event)',
    }))
    selected_data = forms.CharField(widget=forms.HiddenInput())
