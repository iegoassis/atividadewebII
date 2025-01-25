from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Páginas
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def autor(request):
    return render(request, 'autor.html')

def login(request):
    return render(request, 'login.html')

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