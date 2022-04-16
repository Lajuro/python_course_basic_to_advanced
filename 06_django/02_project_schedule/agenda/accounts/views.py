from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


def login(request):
    if auth.get_user(request).is_authenticated:
        messages.success(request, 'Você já está logado')
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Preencha todos os campos')

        user = auth.authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, 'Usuário ou senha incorretos')

        if messages.get_messages(request):
            raise Exception('Validation error')

        auth.login(request, user)
        messages.success(request, 'Logado com sucesso')
        return redirect('dashboard')

    except Exception as e:
        return render(request, 'accounts/login.html', status=400)


def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso')
    return redirect('login')


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

            if messages.get_messages(request):
                raise Exception('Validation error')
        except Exception as e:
            return render(request, 'accounts/register.html', status=400)

        user = User.objects.create_user(username=username, email=email, password=password, first_name=name,
                                        last_name=lastname)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')

    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    try:
        descricao = request.POST.get('descricao')
        nome = request.POST.get('nome')

        if len(descricao) < 5:
            messages.error(request, 'A descrição deve ter no mínimo 5 caracteres')

        if not form.is_valid():
            messages.error(request, 'Erro ao enviar formulário')

        if messages.get_messages(request):
            raise Exception('Validation error')

        form.save()
        messages.success(request, f'Contato {nome} salvo com sucesso!')

        return render(request, 'accounts/dashboard.html', {'form': form})
    except Exception as e:

        return render(request, 'accounts/dashboard.html', {'form': form})
