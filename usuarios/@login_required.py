from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  nome_completo = request.session.get('nome_completo', 'Usuário')
  email = request.session.get('email', 'Sem e-mail')
  tema_preferido = request.session.get('tema_preferido', 'claro')

  contexto = {
    'nome_completo': nome_completo,
    'email': email,
    'tema_preferido': tema_preferido,
  }
  
 return render(request, 'usuarios/home.html')