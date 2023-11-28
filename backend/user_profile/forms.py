from django import forms
from .models import UserProfile, ShippingAdress


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'description', 'phone_number']


class ShippingAdressForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['first_name', 'last_name', 'delivery_adress', 'town', 'pickup_station', 'phone_number']
        
        