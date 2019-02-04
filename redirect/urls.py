from django.urls import path
from . import views

urlpatterns = [
    path('short/', views.index),
    path('short/create/', views.create),
    path('short/<str:user_url>/', views.user_urls),
]