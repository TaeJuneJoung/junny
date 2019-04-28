from django.urls import path
from . import views #오류 무시

app_name ="redirect"

urlpatterns = [
    path('', views.main, name="main"),
    path('short/', views.index, name="index"),
    path('short/create/', views.create, name="create"),
    path('short/<str:user_url>/', views.user_urls, name="user_urls"),
]