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
- **list_editable:** campos que serão utilizados para editar os objetos do modelo. 

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

## Exibindo valores de um único dado em uma view

No arquivo `urls.py`, devemos criar uma rota para a view que exibe um único dado. Por exemplo, para exibir o dado de um `Contato` devemos utilizar a rota `<int:contato_id>`:

```python
# Arquivo: urls.py

# [...]
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>/', views.get_contato, name='get_contato'),
]
```

Depois, no arquivo `views.py`, devemos criar o método que irá renderizar o dado. Para esse exemplo será criado um método com o nome `get_contato`:

```python
# Arquivo: views.py

# [...]
def get_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/get_contato.html', {'contato': contato})
```

Após isso, devemos criar a view que irá renderizar o dado. Para isso, devemos criar um arquivo `get_contato.html` na pasta `templates` da aplicação `contatos`:

```html
<!-- Arquivo: templates/contatos/get_contato.html -->
<h1>{{contato.nome}} {{contato.sobrenome}}</h1>
<dl>
  <dt>ID</dt>
  <dd>{{contato.id}}</dd>

  <dt>Telefone</dt>
  <dd>{{contato.telefone}}</dd>

  <dt>E-mail</dt>
  <dd>{{contato.email}}</dd>

  <dt>Data criação</dt>
  <dd>{{contato.data_criacao|date:'d/m/Y H:i:s'}}</dd>

  <dt>Categoria</dt>
  <dd>{{contato.categoria}}</dd>

  <dt>Descrição</dt>
  <dd>
    {{contato.descricao}}
  </dd>
</dl>
```

### Método `date` do Django
Observe que para a `Data de criação` utilizamos o método `date` do Django, que recebe como parâmetro um formato de data.

Existem as seguintes possibilidades de formatos de `data e hora`:

- **d**: dia, 2 dígitos
- **m**: mês, 2 dígitos
- **Y**: ano, 4 dígitos
- **H**: hora, 2 dígitos
- **i**: minuto, 2 dígitos
- **s**: segundo, 2 dígitos

Pronto, ao acessar a view, verá os dados renderizados conforme o id passada como parâmetro.

Apenas um último detalhe, no arquivo `index.html`, devemos adicionar o link para a view que exibe um único dado. Por exemplo:

```html
<!-- Arquivo: templates/contatos/index.html -->

[...]

<tbody>
{% for contato in contatos %}
<tr>
    <td><a href="{% url 'get_contato' contato.id %}">{{ contato.nome }}</a></td>
    <td>{{ contato.sobrenome }}</td>
    <td>{{ contato.telefone }}</td>
    <td>{{ contato.categoria }}</td>
</tr>
{% endfor %}
</tbody>

[...]
```

O nome 'get_contato' é o nome passado no parâmetro `name` do método `url` da rota `<int:contato_id>` e o `contato.id` é o id do dado que será exibido.

## Levantando erros 404

Para fazer isso é extremamente simples e existem algumas formas de fazer.

Uma maneira é utilizar o método `get_object_or_404` do Django, que retorna um objeto caso ele exista ou gera um erro 404 caso não exista. Por exemplo:

```python
# Arquivo: views.py
from django.shortcuts import render, get_object_or_404
from .models import Contato

def get_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/get_contato.html', {
        'contato': contato
    })

```

Outra maneira é utilizar a exception `DoesNotExist` do Django. Por exemplo:

```python
# Arquivo: views.py

from django.http import Http404
from django.shortcuts import render
from .models import Contato

def get_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/get_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist:
        raise Http404('Contato não encontrado')
```

Qualquer uma dessas maneiras irá te redirecionar para a página de erro 404 do Django.

## Adicionando condicionais

Para trabalhar com condicionais, utilizamos o método `if` do Django. Porém antes vamos adicionar um novo campo ao modelo `Contato`:

```python
# Arquivo: models.py

class Contato(models.Model):
    # [...]
    mostrar = models.BooleanField(default=True)
    
    # [...]
```

> #### **Importante**
> Antes de qualquer coisa, devemos sempre rodar o comando `python manage.py makemigrations` para criar as migrations e então rodar o comando `python manage.py migrate` para executar as migrations, sem isso as alterações não serão refletidas no banco de dados.

No arquivo `admin.py` devemos adicionar o campo `mostrar` na listagem de dados:

```python
# Arquivo: admin.py

# [...]

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'data_criacao', 'categoria', 'mostrar')  # Adicionado aqui
    list_display_links = ('id', 'nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar',)  # Adicionado aqui
    list_filter = ('categoria',)
    search_fields = ('nome', 'email', 'telefone')
    ordering = ('id',)
    list_per_page = 5

```

Foi adicionado o atributo `list_editable` para que o campo `mostrar` seja editável na listagem de dados, sem precisar acessar a página do dado para alterá-lo.

Agora para que os contatos sejam mostrados somente se o campo `mostrar` for verdadeiro, basta adicionar o filtro na listagem de dados:

```html
<!-- Arquivo: templates/contatos/index.html -->

{% for contato in contatos %}
{% if contato.mostrar %}
<tr>
    <td><a href="{% url 'get_contato' contato.id %}">{{ contato.nome }}</a></td>
    <td>{{ contato.sobrenome }}</td>
    <td>{{ contato.telefone }}</td>
    <td>{{ contato.categoria }}</td>
</tr>
{% endif %}
{% endfor %}
```

Desta forma, os dados serão mostrados somente se o campo `mostrar` for verdadeiro.

## Adicionando paginação

Para adicionar uma paginação, o Django já se dispõe de uma biblioteca chamada `Paginator` que permite fazer isso.

Para isso, vamos abrir o arquivo `views.py` e importar a biblioteca `Paginator`:

```python
# Arquivo: views.py

from django.core.paginator import Paginator

```

Então em nossa view `index`, vamos criar uma nova variavel com o nome `paginator` que recebe como valor o objeto `Paginator`:

```python
# Arquivo: views.py
    
    # [...]
    def index(request):
        contatos = Contato.objects.all()
        paginator = Paginator(contatos, 3)
    # [...]

```

Após isso, vamos pegar da URL o número da página passado no `query_params`, e com esse dado, vamos usar para pegar os dados da página e salvar na variavel `contatos`:

```python
# Arquivo: views.py
    
    # [...]
    def index(request):
        contatos = Contato.objects.all()
        paginator = Paginator(contatos, 3)
        
        page = request.GET.get('page')
        contatos = paginator.get_page(page)
    # [...]

```

Observe que no `request.GET.get('page')` estamos pegando o parâmetro `page` da URL, esse nome pode ser qualquer nome desejado, porém caso seja alterado, é preciso referenciar corretamente no HTML.

Para adicionar a paginação na página, abra o arquivo `templates/contatos/index.html` e adicione o código abaixo:

```html
<!-- Arquivo: templates/contatos/index.html -->

<!-- [... Após a tag de fechamento </table> ...] -->
<nav aria-label="Navegação da página">
    <ul class="pagination">
        {% for pagina in contatos.paginator.page_range %}
        {% if contatos.number == pagina %}
        <li class="page-item active"><a class="page-link" href="?page={{pagina}}">{{pagina}}</a></li>
        {% else %}
        <li class="page-item"><a class="page-link" href="?page={{pagina}}">{{pagina}}</a></li>
        {% endif %}
        {% endfor %}
    </ul>
</nav>
<!-- [...] -->
```

Utilizamos o `page_range` para recuperar a lista de páginas, e fizemos uma verificação para saber se o número atual da paginação, é a página que estamos, se sim, destaca-se com a classe `active` e se não, não se destaca.

Todo esse HTML foi recuperado do exemplo do framework Bootstrap.

## Ordenando e filtrando valores

Para ordenar e filtrar valores no Django, é extremamente simples, basta trocar de `Contatos.objects.all()` por `Contatos.objects.order_by('nome')`, e para filtrar basta adicionar o filtro, ficando então `Contatos.objects.order_by('nome').filter(mostrar=True)`.

Para ordernar de forma decrescente basta adicionar o parâmetro `-` antes do campo que deseja ordenar. 

**Por exemplo:** `Contatos.objects.order_by('-nome')`.


> ## Correção de exibição de contato que está como `mostrar = False`
> 
> Caso tente acessar uma página de um contato que está como `mostrar = False`, você perceberá que está conseguindo abrir e isso não deveria acontecer. Para que isso não ocorra, é bem simples.
> 
> Na view `get_contato`, vamos adicionar um filtro para que seja mostrado somente os contatos que estão com o campo `mostrar` como `True`, caso contrário, retornará um página de erro 404.
>
> ```python
> # Arquivo: views.py
>     
> # [...]
> def get_contato(request, contato_id):
>     contato = get_object_or_404(Contato, id=contato_id)
>     if not contato.mostrar:
>         raise Http404("Contato não encontrado")
> 
>     return render(request, 'contatos/get_contato.html', {
>         'contato': contato
>     })
> # [...]
> 
> ```

