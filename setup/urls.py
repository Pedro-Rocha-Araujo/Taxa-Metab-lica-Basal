from django.urls import path
from app_tmb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resultado/', views.resultado, name='resultado')
]
