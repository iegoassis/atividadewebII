from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Páginas
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

@login_required
def autor(request):
    return render(request, 'autor.html')

@login_required
def calcular_view(request):
    return render(request, 'calcular.html')

@login_required
@csrf_exempt
def calcular(request):
    if request.method == 'POST':
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operacao = request.POST.get('operacao')

        if operacao == 'soma':
            resultado = numero1 + numero2
            explicacao = f"Soma de {numero1} e {numero2}"
        elif operacao == 'subtracao':
            resultado = numero1 - numero2
            explicacao = f"Subtração de {numero1} e {numero2}"
        elif operacao == 'multiplicacao':
            resultado = numero1 * numero2
            explicacao = f"Multiplicação de {numero1} e {numero2}"
        elif operacao == 'divisao':
            if numero2 == 0:
                return render(request, 'resultado.html', {
                    'mensagem': "Divisão por zero não é permitida."
                })
            resultado = numero1 / numero2
            explicacao = f"Divisão de {numero1} por {numero2}"
        else:
            return HttpResponse("Operação inválida.")

        return render(request, 'resultado.html', {
            'explicacao': explicacao,
            'resultado': resultado
        })

    return HttpResponse("Método HTTP não suportado.")

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Você já pode fazer login.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar usuário: {str(e)}")
            return redirect('registro')

    return render(request, 'registro.html')

def fazer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            next_url = request.POST.get('next', 'home')
            messages.success(request, "Login realizado com sucesso!")
            return redirect(next_url)
        else:
            messages.error(request, "Credenciais inválidas.")

    return render(request, 'login.html', {'next': request.GET.get('next', '')})

def fazer_logout(request):
    auth_logout(request)
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect('login')