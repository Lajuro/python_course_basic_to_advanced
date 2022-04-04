from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 3)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def get_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/get_contato.html', {
        'contato': contato
    })

