from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        try:
            if not name or not lastname or not email or not username or not password or not password_confirmation:
                messages.error(request, 'Preencha todos os campos')

            if len(name) < 2 or len(lastname) < 2:
                messages.error(request, 'Nome e sobrenome devem ter mais de 2 caracteres')

            if len(username) < 6:
                messages.error(request, 'O nome de usuário deve ter no mínimo 6 caracteres')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'O nome de usuário já existe')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'O email já existe')

            try:
                validate_email(email)
            except ValidationError as e:
                messages.error(request, 'Email inválido')

            if len(password) < 8:
                messages.error(request, 'A senha deve ter no mínimo 8 caracteres')

            if password != password_confirmation:
                messages.error(request, 'As senhas não conferem')
                return render(request, 'accounts/register.html', status=400)
        except Exception as e:
            return render(request, 'accounts/register.html', status=400)

        user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=lastname)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
