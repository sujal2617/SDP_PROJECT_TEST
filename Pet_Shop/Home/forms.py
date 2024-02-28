from django import forms
from .models import ContactMessage,Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# forms.py


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, required=False)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['name','price','description','digital','image','age','height','life_expectancy']