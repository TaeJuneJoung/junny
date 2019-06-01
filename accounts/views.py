from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('shorts:main')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/form.html', {'form':form})
    else:
        return redirect('shorts:main')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('shorts:main')