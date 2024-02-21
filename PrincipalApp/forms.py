from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, Form, Select 


class UsuarioForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'input pl-10','placeholder':'Username'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input pl-10','placeholder':'Password'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'input pl-10','placeholder':'Confirm Password'}))
    first_name = forms.CharField(label='Nombre', max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'input pl-10','placeholder':'Name'}))
    last_name = forms.CharField(label='Apellido', max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'input pl-10','placeholder':'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'input pl-10','placeholder':'Email'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input pl-10','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input pl-10','placeholder':'Password'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )