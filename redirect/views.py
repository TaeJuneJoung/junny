from django.shortcuts import render, redirect
from .models import Junny
# Create your views here.

def index(request):
    return render(request, "redirect/index.html")
    
def create(request):
    long_url = request.POST.get("long_url")
    user_short_url = request.POST.get("short_url")
    user_short_url = user_short_url.split("http://junny-jtj0525.c9users.io:8080/short/")
    Junny.objects.create(long_url=long_url, short_url=user_short_url[1])
    return redirect("/short/")
    
def user_urls(request, user_url):
    junny = Junny.objects.get(short_url=user_url)
    long_url = junny.long_url
    return redirect(f"{long_url}")
    