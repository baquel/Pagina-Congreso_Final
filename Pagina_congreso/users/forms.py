from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField()
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    image = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ["email", "last_name", "first_name", "image"]
        help_text = {k: "" for k in fields}