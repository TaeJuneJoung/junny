from django.shortcuts import render, redirect
from .models import Junny
# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'shorts/main.html')
    return render(request, 'main.html')

def list(request, user_id):
    #유저정보로 그 사람이 만든 URL주소 가져오기
    return render(request, "shorts/index.html")
    
def create(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        user_short_url = request.POST.get("short_url")
        domain_url = request.POST.get("domain_url")
        user_short_url = user_short_url.split(domain_url)
        Junny.objects.create(long_url=long_url, short_url=user_short_url[1], user=request.user)
    return redirect("shorts:main")
    
def user_urls(request, user_url):
    try:
        junny = Junny.objects.get(short_url=user_url)
        long_url = junny.long_url
    except Junny.DoesNotExist:
        return render(request, 'error_404.html')
    return redirect(f"{long_url}")