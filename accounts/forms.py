from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'