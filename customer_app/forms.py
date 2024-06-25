from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Customer, Product
from django import forms


class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': ' mb-2 border-indigo-500 rounded-lg font-medium'}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'mb-2 border-indigo-500 rounded-lg font-medium'}))
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['description', 'tag']


class CustomerForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mb-2 border-indigo-500 rounded-lg font-medium'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'mb-2 border-indigo-500 rounded-lg font-medium'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'mb-2 border-indigo-500 rounded-lg font-medium'}))
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreteUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']