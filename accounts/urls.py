from django.urls import path
from . import views #오류 무시

app_name ="accounts"

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]