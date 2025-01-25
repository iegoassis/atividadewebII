from django.contrib.auth import authenticate, login

def fazer_login(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      # Autenticar o usuário
      user = authenticate(request, username=username, password=password)

      if user is not None:
          # Fazer login
          login(request, user)

        request.session['nome_completo'] = username
        request.session['email'] = user.email
        request.session['tema_preferido'] = 'claro'
    
        messages.success(request, "Login realizado com sucesso!")
          return redirect('home')
      else:
          # Exibir mensagem de erro
          messages.error(request, "Credenciais inválidas.")
          return redirect('login')

  # Renderizar a página de login
  return render(request, 'usuarios/login.html')