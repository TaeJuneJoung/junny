from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'login_id form-control','placeholder': 'Enter User ID'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'login_pw form-control','placeholder':'Enter User Password'}))
    class Meta:
        model = User
        fields = ('username, password')
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'