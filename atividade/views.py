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

def autor(request):
    return render(request, 'autor.html')

def calcular_view(request):
    return render(request, 'calcular.html')

# Função com CSRF para cálculo
@csrf_exempt
def calcular(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operacao = request.POST.get('operacao')

        # Verificando a operação e calculando o resultado
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

        # Renderizando o resultado
        return render(request, 'resultado.html', {
            'explicacao': explicacao,
            'resultado': resultado
        })

    return HttpResponse("Método HTTP não suportado.")

# Registro de usuário
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return redirect('registro')

        # Criar o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Exibir mensagem de sucesso
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    # Renderizar a página de registro
    return render(request, '/registro.html')

# Login de usuário
def fazer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Fazer login
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            # Exibir mensagem de erro
            messages.error(request, "Credenciais inválidas.")
            return redirect('login')

    # Renderizar a página de login
    return render(request, 'login.html')

# Logout de usuário
def fazer_logout(request):
    auth_logout(request)
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect('login')