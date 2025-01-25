from django.contrib.auth import logout
from django.shortcuts import redirect

def fazer_logout(request):
    logout(request)
    request.session.flush()
    messages.success(request, "Você saiu da conta.")
    return redirect('login')