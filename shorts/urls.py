from django.urls import path
from . import views #오류 무시

app_name ="shorts"

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:user_id>/list', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('<str:user_url>/', views.user_urls, name="user_urls"),
]