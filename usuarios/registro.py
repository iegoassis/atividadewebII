from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
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
      user = User.objects.create_user(username=username,email=email,password=password)
      user.save()

      # Exibir mensagem de sucesso
      messages.success(request, "Cadastro realizado com sucesso! Faça login.")
      return redirect('login')

  # Renderizar a página de registro
  return render(request, 'usuarios/registro.html')
