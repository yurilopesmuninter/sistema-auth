from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_django
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        userExists = User.objects.filter(username=username).first()
        if userExists:
            return HttpResponse('Já existe')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save
        return HttpResponse('Usuário cadastrado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect(plataforma)
        else:
            return HttpResponse('Email ou senha inválidos')

@login_required(login_url='/auth/login/')
def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'plataforma.html')

def redefinir_senha(request):
    if request.method == "GET":
        return render(request, 'altera_senha.html')
    else:
        username = request.POST.get('username')
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        try:
            user = User.objects.get(username=username)
            if user.check_password(senha_antiga):
                user.set_password(nova_senha)
                user.save()
                return HttpResponse('A senha foi alterada com sucesso!')
            else:
                return HttpResponse('A senha antiga não está correta!')
        except User.DoesNotExist:
            return HttpResponse('Usuário não encontrado!')

@login_required(login_url='/auth/login/')
def logout(request):
    logout_django(request)
    return redirect(login)
