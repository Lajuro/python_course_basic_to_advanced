from django.shortcuts import render


def home(request):
    # Renderiza a página principal
    return render(request, 'paginas/home.html', {'title': 'Home'})


def about(request):
    # Renderiza a página sobre
    return render(request, 'paginas/about.html', {'title': 'Sobre'})
