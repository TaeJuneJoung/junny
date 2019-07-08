from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm

# Create your views here.
def join(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('shorts:main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/form.html', {'form':form})

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, request.POST)
            if form.is_valid():
                print(form)
                auth_login(request, form.get_user())
                return redirect('shorts:main')
        else:
            form = CustomAuthenticationForm()
        return render(request, 'accounts/form.html', {'form':form})
    else:
        return redirect('shorts:main')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('shorts:main')
    
def user_page(request, user_id):
    User = get_user_model()
    user_info = get_object_or_404(User, pk=user_id)
    return render(request, 'accounts/my_page.html', {'user_info':user_info})