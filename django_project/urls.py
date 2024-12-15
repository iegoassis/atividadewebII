from django.urls import path
from atividade import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('calcular/', views.calcular_view, name='calcular_view'),  # Exibe o formulário
    path('resultado/', views.calcular, name='resultado'),  # Processa os cálculos
    path('autor/', views.autor, name='autor'),
]