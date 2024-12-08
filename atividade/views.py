from django.http import HttpResponse

# Create your views here.


def home(request):
  msg = """
  <!DOCTYPE html>
  <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello World</title>
    </head>
    <body>
      <h1>Seja bem vindo a atividade</h1>
      <p>Este é um exemplo de atividade</p>
    </body>
    </html>
    
  """
  return HttpResponse(msg)
