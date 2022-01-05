from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('llamada-api/', views.hello, name='hello-users'),
]
