from django import urls
from django.urls import path
from usuarios import views
urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),
    path('home/', views.home, name='home'),
]