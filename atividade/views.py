from unittest import removeHandler
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from atividade import views
from atividade import models
from django.shortcuts import render


def home(request):
    return render (request, 'atividade/home.html')

def index(request):
    return render (request, 'atividade/index.html')
    
def calcular(request):
    return render (request, 'atividade/calcular.html')

def calcular (request):
    return render (request, 'atividade/calcular.html')
    
def autor(request):
    return render (request, 'atividade/autor.html')

