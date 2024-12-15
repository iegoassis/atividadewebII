from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Funções de visualização para as páginas estáticas
def home(request):
    return render(request, 'atividade/home.html')

def index(request):
    return render(request, 'atividade/index.html')

def autor(request):
    return render(request, 'atividade/autor.html')

def calcular_view(request):
    return render(request, 'atividade/calcular.html')

# Função para cálculo com CSRF
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
                # Tratando divisão por zero
                msg = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Erro</title>
                </head>
                <body>
                    <h1>Erro</h1>
                    <p>Divisão por zero não é permitida. Tente novamente.</p>
                    <a href="/index/">Voltar</a>
                </body>
                </html>
                """
                return HttpResponse(msg)
            resultado = numero1 / numero2
            explicacao = f"Divisão de {numero1} por {numero2}"
        else:
            # Operação inválida
            return HttpResponse("Operação inválida.")

        # Montando a resposta HTML
        msg = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resultado</title>
        </head>
        <body>
            <h1>Resultado do Cálculo</h1>
            <p>Você realizou a seguinte operação:</p>
            <p>{explicacao}</p>
            <p><strong>Resultado:</strong> {resultado}</p>
            <a href="/index/">Voltar</a>
        </body>
        </html>
        """
        return HttpResponse(msg)
    else:
        # Caso não seja uma requisição POST
        return HttpResponse("Método HTTP não suportado.")
