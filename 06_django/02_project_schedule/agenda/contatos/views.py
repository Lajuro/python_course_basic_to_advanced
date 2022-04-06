from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 3)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    print(termo)

    if termo is None or not termo:
        messages.add_message(request, messages.DEBUG, 'Informe um termo para busca')
        return redirect('index')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) | Q(categoria__nome__icontains=termo),
        mostrar=True
    ).order_by('-id')

    paginator = Paginator(contatos, 3)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })


def get_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404("Contato não encontrado")

    return render(request, 'contatos/get_contato.html', {
        'contato': contato
    })
