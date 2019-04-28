from django.shortcuts import render, redirect
from .models import Junny
from .forms import JunnyForm
# Create your views here.

def main(request):
    return redirect("redirect:index")

def index(request):
    return render(request, "redirect/index.html")
    
def create(request):
    if request.method == "POST":
    #     form = JunnyForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("redirect:index")
    # else:
    #     form = JunnyForm()
    # return render(request, "redirect/index.html", {"form":form})
        long_url = request.POST.get("long_url")
        user_short_url = request.POST.get("short_url")
        user_short_url = user_short_url.split("http://junny-jtj0525.c9users.io:8080/short/")
        Junny.objects.create(long_url=long_url, short_url=user_short_url[1])
        print(long_url, user_short_url)
    return redirect("redirect:index")
    
def user_urls(request, user_url):
    junny = Junny.objects.get(short_url=user_url)
    long_url = junny.long_url
    return redirect(f"{long_url}")