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

## Criando os Models

### Banco de Dados

Para configuração do banco de dados do Django, no arquivo `settings.py` na seção `DATABASES`, você irá encontrar as configurações do banco de dados, por padrão o Django utiliza o banco de dados `sqlite3`.

### Modelo de Contato

Para criar o modelo de contato, devemos no arquivo `models.py` da aplicação `contatos`, adicionar o seguinte:

```python
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
```

Observe que foi criado a classe `Categoria` e a classe `Contato`, e que estão relacionadas.

Os tipos de dados que podem ser utilizados no Django são:

- **CharField:** campo de texto
- **TextField:** campo de texto grande
- **EmailField:** campo de e-mail
- **DateTimeField:** campo de data e hora
- **ForeignKey:** campo de chave estrangeira

Após a criação do modelo, devemos rodar o seguinte comando:

```bash
python manage.py makemigrations
python manage.py migrate
```

Dessa forma, o Django criará o banco de dados e a estrutura de tabelas necessárias para o modelo.

## Django Admin

Para acessar o Django Admin, devemos acessar a URL `http://localhost:<porta>/admin/`.

### Criando um super usuário

Para criar um super usuário, devemos rodar o seguinte comando:

```bash
python manage.py createsuperuser
```

Será solicitado que digite o nome de usuário, e-mail, senha e a confirmação da senha, caso a senha seja fora dos padrões, será perguntado se deseja fazer o bypass da validação e criar o usuário mesmo assim, caso sim, digite `y`.

Com o superuser criado, agora poderá acessar o Django Admin.

### Criando um modelo no Django Admin

No arquivo `admin.py` da aplicação `contatos`, adicionar o seguinte:

```python
from django.contrib import admin
from .models import Categoria, Contato

admin.site.register(Categoria)  # Registrando a classe `Categoria` no Django Admin
admin.site.register(Contato)  # Registrando a classe `Contato` no Django Admin
```

Ao fazer isso, quando acessar o Django Admin, será apresentado os modelos `Categoria` e `Contato` da aplicação `contatos`.

Após isso, você pode personalizar como será exibido os campos do modelo `Categoria` e `Contato` no Django Admin. Para isso, devemos criar uma classe para cada model com o sufixo `Admin`.

```python
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
```

Abaixo uma breve descrição do que é cada uma das propriedades:

- **list_display:** lista de campos que serão exibidos na listagem dos objetos do modelo.
- **search_fields:** campos que serão utilizados para pesquisar os objetos do modelo.
- **list_filter:** campos que serão utilizados para filtrar os objetos do modelo.
- **ordering:** campos que serão utilizados para ordenar os objetos do modelo.

Outra coisa simples de se fazer, é definir como será exibido o modelo no Django Admin. Para isso, no modelo devemos ir para o model dele e adicionar o método `__str__`:

```python
def __str__(self):
    return self.nome
```

Isso pode ser feito para que exiba de uma forma melhor, pois por padrão irá exibir o nome do modelo, por exemplo, no modelo `Categoria`, será exibido `Categoria: <nome>`.

## Exibindo valores nas views

Para exibir valores nas views, devemos abrir o arquivo `views.py` da aplicação `contatos`, e no método que é renderizado, passamos um terceiro parâmetro, que é um dicionário, que será utilizado para passar valores para a view.

Mas antes, é importante importar o modelo `Contato` e no método que é renderizado, adicionar uma variável `contatos` que receberá o objeto `Contato` que foi passado como parâmetro. Por exemplo:

```python
# Arquivo: views.py
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {'contato': contato})
```

E na view, devemos utilizar a variável `contatos` para exibir os valores. Por exemplo:

```html
<!-- Arquivo: templates/contatos/index.html -->
<table>
    <thead>
        <tr>
            <th>Nome</th>
            <th>Sobrenome</th>
            <th>E-mail</th>
            <th>Categoria</th>
        </tr>
    </thead>
    <tbody>
        {{ for contato in contatos }}
        <tr>
            <td><a href="/{{contato.id}}">{{contato.nome}}</a></td>
            <td>{{ contato.sobrenome }}</td>
            <td>{{ contato.email }}</td>
            <td>{{ contato.categoria }}</td>
        </tr>
        {{ endfor }}
    </tbody>
</table>
```

Com isso, será renderizado uma tabela com os valores do modelo `Contato`.