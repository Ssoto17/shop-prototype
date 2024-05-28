from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Location

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']#,'email']

class InventoryItemForm(forms.ModelForm):
    locations = forms.ModelChoiceField(queryset=Location.objects.all(), initial = 0)
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'locations', 'barcode', 'notes']



