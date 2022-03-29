# Agenda - Projeto em Django

Este projeto será uma agenda feita em Django onde será utilizado a criação de models, compreensão do Django Admin,
levantamento de erros 404, condicionais em Django, pillow, Django messages, sistema de login, logout e criação de um
Dashboard.

## Iniciando o projeto

Para iniciar o projeto em Django, execute o seguinte comando:

```shell
  django-admin startproject agenda
```

Após isso, vamos criar um aplicativo com o nome `contatos`, para isso, execute o seguinte comando:

```shell
  python manage.py startapp contatos
```

### Lembre-se

- Adicionar o `ContatosConfig` no arquivo `settings.py` do projeto em INSTALLED_APPS.
- Adicionar o include do `contatos.urls` no arquivo `urls.py` do projeto.

Crie um arquivo `urls.py` dentro do diretório `contatos` e adicione o seguinte:

```python
from django.conf.urls import url
from contatos import views

urlpatterns = [
    url('', views.index, name='index'),
]
```

No arquivo `views.py` crie o seguinte:

```python
from django.shortcuts import render


def index(request):
    return render(request, 'contatos/index.html')
```

Crie a pasta `templates` dentro do diretório `contatos`, dentro de `templates` crie uma pasta `contatos` e então crie o
arquivo `index.html` dentro da pasta `contatos`.

Após isso, vamos para a criação da pasta templates na raíz do projeto, pois nela teremos o arquivo `base.html` que será
o template base para todas as páginas.

Dentro da pasta `templates` da pasta raíz, crie uma pasta `static` que será onde ficará armazenado os arquivos
estáticos.

Não esqueça de no arquivo `settings.py` adicionar em `DIRS` de `TEMPLATES` o seguinte:

```python
TEMPLATES = [
    {
        # [...]
        'DIRS': [BASE_DIR / 'templates'],  # Adicione o caminho para o diretório `templates`
        # [...]
    },
]
```

Isso fará com que o projeto fique configurado em olhar dentro desta pasta ao utilizar o template base.

Além disso, nesse mesmo arquivo, para que os arquivos estáticos sejam acessados, adicione a constante `STATICFILES_DIRS`
e nela adicione o seguinte:

```python
STATICFILES_DIRS = [BASE_DIR / 'templates/static']
```

## Template Base - Base.html

Após isso, devemos configurar o arquivo `base.html`, iremos criar parcias de código para o template base.

### Head

Para o cabeçalho, foi extraído a seguinte parte:

```html
{% load static %}

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">

<!-- Bootstrap core CSS -->
<link href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">
```

> Observe que é necessário utilizar o `load static` para que o Django possa acessar os arquivos estáticos, pois estamos utilizando essa referência ao importar a estilização do Bootstrap.

### Navigation

Para a navegação, foi extraído a seguinte parte:

```html
<!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
        <a class="navbar-brand" href="{% url 'index' %}">Agenda</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    </div>
</nav>
```

> Observe que na âncora `<a>`, utilizamos o `url` para referenciar ao namespace `index` que foi criado no arquivo `urls.py`.

### Configurando o arquivo `base.html`

No arquivo `base.html`, nas partes em que estão os cabeçalhos e a navegação, devemos adicionar o código abaixo:

```html
[...]

<!-- Cabeçalho -->
{% include 'partials/_head.html' %}

[...]

<!-- Navegação -->
{% include 'partials/_nav.html' %}

[...]

```

No conteúdo da página, podemos utilizar o sistema de blocos do Django, para isso adicione o seguinte:

```html
<!-- Conteúdo da página -->
{% block 'conteudo' %}{% endblock %}
```

Ao fazer isso, poderá utilizar no arquivo `index.html`, criado para a rota principal do app `contatos`, o seguinte:

```html
{% extends 'base.html' %}

{% block 'conteudo' %}
<!-- Conteúdo da página -->
{% endblock %}
```

No conteúdo da página, foi adicionado o seguinte:

```html
<h1 class="mt-5">Minha agenda</h1>

<table class="table">
    <thead>
    <tr>
        <th>Nome</th>
        <th>Sobrenome</th>
        <th>Telefone</th>
        <th>Categoria</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>
            <a href="#"> João</a>
        </td>
        <td>Miranda</td>
        <td>35 9 5555-5555</td>
        <td>Família</td>
    </tr>
    <tr>
        <td>
            <a href="#"> Leandro</a>
        </td>
        <td>Moreira</td>
        <td>35 9 8888-5555</td>
        <td>Família</td>
    </tr>
    <tr>
        <td>
            <a href="#"> Fátima</a>
        </td>
        <td>Oliveira</td>
        <td>35 9 9999-4352</td>
        <td>Conhecidos</td>
    </tr>
    </tbody>
</table>
```

Após ter feito isso, pode rodar o comando `python manage.py runserver` para verificar se o app está funcionando.