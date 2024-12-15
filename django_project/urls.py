from django.contrib import admin
from django.urls import path
from atividade import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('calcular/', views.calcular, name='calcular'),
    path('autor/', views.autor, name='autor')
]
