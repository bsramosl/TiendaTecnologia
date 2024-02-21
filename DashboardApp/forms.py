from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, Form, Select
from .models import *
from django.forms import DateInput, ModelForm, ModelChoiceField, Form, Select, TextInput

class BusinessForm(forms.ModelForm): 
   
    class Meta:
        model = BusinessModel
        fields ='__all__'
        widgets={
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                }
             
            ),'telephone': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                }
            ),'phone': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                }
            ),
            'address': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),           
                          
        }



class CategoryForm(ModelForm):

    class Meta:
        model = CategoryModel
        fields = ('__all__')

class ProductForm(ModelForm):

    class Meta:
        model = ProductModel
        fields = ('__all__')

class CartForm(ModelForm):

    class Meta:
        model = CartModel
        fields = ('__all__')