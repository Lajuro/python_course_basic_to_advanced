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

## Adicionando um campo de pesquisa

Para adicionar a funcionalidade de pesquisa na listagem dos contatos, podemos fazer o seguinte, primeiro no arquivo `base.html`, iremos adicionar o seguinte HTML:

```html
<!-- Arquivo: base.html -->

<div class="col-lg-12">
    <!-- O formulário foi inserido a partir daqui -->
    <br><br>
    <form method="get" action="{% url 'busca' %}">
        <div class="form-group row">
            <div class="col-12">
                <input class="form-control"
                       type="search" value="{{ request.GET.termo }}"
                       id="search-input"
                       placeholder="Digite sua pesquisa"
                       name="termo">
            </div>
        </div>
    </form>
    <!-- O formulário encerra aqui -->

    {% block 'conteudo' %}{% endblock %}
</div>

```

Com esse formulário, já poderemos trabalhar com a pesquisa, observe que o `action` aponta para a url `busca`, e o `method` é `get`, ou seja, o formulário será enviado por GET, que é basicamente passar os parâmetros da pesquisa na URL.

Além disso, observe que o `value` do input está como `{{ request.GET.termo }}`, ou seja, o valor do input será o que está na URL com o nome `termo`.

### Configurações necessárias

Para funcionar a pesquisa, é necessário alguns ajustes, começando pelo arquivo `urls.py`, nele iremos adicionar a url `busca`:

```python
# Arquivo: urls.py

urlpatterns = [
    # [...]
    path('busca/', views.busca, name='busca'),
    # [...]
]

```

No arquivo `views.py`, adicionaremos o seguinte:

```python
# Arquivo: views.py

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    print(termo)

    if termo is None:
        termo = ''

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

```

Essa função que fará a mágica acontecer, só é necessário fazer os imports necessários:

```python
# Arquivo: views.py

from django.db.models import Q, Value
from django.db.models.functions import Concat

# [...]

```

Na função `busca`, primeiro iremos pegar o termo que está na URL, e então criamos uma variável que irá montar a estrutura do `nome_completo`.

Caso o termo não seja informado, o valor da variável será `''`, ou seja, não irá filtrar nada, isso para não quebrar na busca, pois `None` não é um valor válido para a pesquisa.

Depois iremos fazer uma consulta no banco de dados, porém ao invés de usar o `order_by`, `all` ou `filter`, iremos usar o `annotate` para adicionar um campo que será usado na consulta, e esse campo será o `nome_completo`, que foi montado com o `Concat` do Django.

No filtro, utilizamos o `Q`, nele podemos fazer consultas mais complexas, podendo usar o `|` para combinar as consultas, ou seja, se o termo for encontrado no nome, ou no telefone, ou na categoria, ou seja, se o termo estiver em qualquer um dos campos, então o contato será mostrado.

Observe que é utilizando o `__icontains` para fazer a pesquisa, ou seja, a pesquisa irá verificar se o termo está contido no nome, telefone ou categoria. Sendo que a `categoria` é um campo do tipo `ForeignKey`, então a pesquisa irá verificar se o nome da categoria está contido no termo, observe que ficou `categoria__nome__icontains` e não `categoria__icontains`, de resto, tudo ficou igual.

Agora que concluímos a configuração da função responsável por exibir a view, lembre-se de criar a view `busca.html` em `templates/contatos/`, e adicionar o seguinte:

```html
<!-- Arquivo: busca.html -->

{% extends "contatos/index.html" %}
```

Ele será exatamente igual ao `index.html`, sem nenhuma diferença.

No arquivo `index.html`, foram feitas algumas correções, a primeira é que não precisa mais do `if` que verifica se o `contato.mostrar` é `True`, e a segunda foi no link da paginação, foi feito o seguinte:

```html
<!-- Arquivo: index.html -->

<nav aria-label="Paginação">
    <ul class="pagination">
        {% for pagina in contatos.paginator.page_range %}
        {% if contatos.number == pagina %}
        <li class="page-item active"><a class="page-link" href="?page={{pagina}}{% if request.GET.termo %}&termo={{ request.GET.termo }}{% endif %}">{{pagina}}</a></li>
        {% else %}
        <li class="page-item"><a class="page-link" href="?page={{pagina}}{% if request.GET.termo %}&termo={{ request.GET.termo }}{% endif %}">{{pagina}}</a></li>
        {% endif %}
        {% endfor %}
    </ul>
</nav>

```

O `href` ficou como `href="?page={{pagina}}{% if request.GET.termo %}&termo={{ request.GET.termo }}{% endif %}"`, isso para que o link seja a página e, caso o termo seja informado, ele seja passado como parâmetro da URL também, para que nos casos em que não for passado o termo da pesquisa fique como `termo=`, que é desnecessário.

## Como adicionar imagens

Para adicionar imagens, primeiro temos que ir no arquivo `urls.py` do projeto e adicionar o seguinte:

```python
# Arquivo: urls.py
# [...]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

Foram feitos os imports necessários, e no final do `urlpatterns`, adicionamos o `static` para que a imagem seja exibida na página.

Além disso, estamos fazendo referencia a duas variáveis do Django, `settings.MEDIA_URL` e `settings.MEDIA_ROOT`, que são as variáveis que nos dizem o caminho para a pasta de imagens, e o caminho para a pasta de imagens consecutivamente.

Então, no aquivo `settings.py`, temos que adicionar o seguinte, preferencialmente na seção `static`:

```python
# Arquivo: settings.py

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'templates/static']

#### Adicione as variáveis abaixo ####
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

```

Certo, agora temos tudo configurado no projeto, então podemos seguir com a adição de um novo campo no model `Contato`:

```python
# Arquivo: models.py

class Contato(models.Model):
    # [...]
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True, null=True)
```

Agora que configuramos o model, temos que rodar os comandos `python manage.py makemigrations` e `python manage.py migrate` para que o campo seja adicionado no banco de dados. Ao fazer isso, poderá ver que agora existe um campo a mais ao acessar algum contato no `Django Admin`.

Já existe a funcionalidade de adicionar imagem agora, mas agora temos que adicionar a imagem em algum usuário e configurar para ela ser exibida quando formos abrir um contato.

No arquivo `get_contato.html`, temos que adicionar o seguinte:

```html
<!-- Arquivo: get_contato.html -->

<!-- [...] -->
<h1 class="mt-5">{{contato.nome}} {{contato.sobrenome}}</h1>

<!-- Adicionar o que está abaixo -->
{% if contato.foto %}
<p>
    <img src="{{contato.foto.url}}" style="max-width: 250px;"/>
</p>
{% endif %}
<!-- Termina aqui o que foi inserido -->
<dl>
    <dt>ID</dt>
    <dd>{{contato.id}}</dd>
    
    <!-- [...] -->

```

Após fazer isso, já deverá conseguir ver a imagem nos contatos que foi adicionado uma imagem.

## Adicionar mensagens de feedback ao usuário

Existe algo bem legal que pode ser feito, que é definir mensagens de feedback de uma determinada açao do usuário, para isso o Django disponibiliza uma função chamada `messages.add_message`, que recebe como parâmetro o request, o tipo de mensagem e o texto da mensagem.

Para ficar de uma maneira mais dinâmica, vamos adicionar no arquivo `settings.py` o seguinte:

```python
# Arquivo: settings.py

# Mensagens
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.DEBUG: 'dark',
    messages.SUCCESS: 'success',
    messages.INFO: 'info'
}

```

Essas são as constantes que serão utilizadas para determinar o tipo de mensagem que queremos exibir.

Vamos criar uma `partial` que irá exibir as mensagens existentes, crie então na pasta `partials` da pasta `templates` na raíz do projeto, um arquivo chamado `_messages.html`:

```html
<!-- Arquivo: partials/_messages.html -->

{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}" role="alert">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}

```

Observe que verificamos se existe alguma variável `messages` na requisiçao, se tiver, para ser feito um loop em todas elas e exibí-las. Já nos alertas, exibe o tipo de alerta através do atributo `tags` que está dentro do objeto `message`. Já a mensagem fica dentro do próprio objeto `message`.

### Configurando o template `base.html`

No arquivo `base.html`, temos que adicionar o seguinte:

```html
<!-- Arquivo: base.html -->

<!-- [...] -->
</form>

{% include 'partials/_messages.html' %}

{% block 'conteudo' %}{% endblock %}
<!-- [...] -->
</div>

```

### Configurando a view `busca`

No arquivo `views.py`, temos que adicionar o seguinte:

```python
# Arquivo: views.py

# [...]
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# [...]

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    print(termo)
    
    ### Foi modificado a verificação abaixo para dar um feedback ao usuário caso o campo estiver vazio
    if termo is None or not termo:
        messages.add_message(request, messages.DEBUG, 'Informe um termo para busca')
        return redirect('index')
    ### Termina aqui a modificação

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

```

Observe que foi utilizado o `messages` do Django e nele foi utilizado o método `add_message` para adicionar uma mensagem de feedback ao usuário, onde o primeiro parâmetro é o request, o segundo é o tipo de mensagem e o terceiro é o texto da mensagem.

Em seguida é feito o redirecionamento para a página inicial utilizando o método `redirect`, o parâmetro é o `name` da rota que será redirecionada.

## Como deixar o Django em Português

Abra o arquivo `settings.py` e adicione o seguinte:

```python
# Arquivo: settings.py

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True
```

- `LANGUAGE_CODE` é a variável que define o idioma padrão do Django, no caso, o Português.
- `TIME_ZONE` é a variável que define a zona padrão do Django, no caso, a zona de São Paulo.
- `USE_I18N` é a variável que define se o Django deve ou não utilizar o sistema de internacionalização.
- `USE_TZ` é a variável que define se o Django deve ou não utilizar o sistema de fuso horário.

> Por padrão, o **Django** utiliza o idioma `en-US` e o fuso horário `UTC`.

## Configurando um Sistema de Login

### Configurações iniciais
Para começar essa configuração de um sistema de login, vamos criar uma nova aplicação chamada `accounts`, que será aplicada ao projeto. Para isso, rodamos o comando:

```bash
$ python manage.py startapp accounts
```

Após criar a aplicação `accounts`, vamos fazer as configurações inicias, que são:

- No arquivo `settings.py` do projeto, em `INSTALLED_APPS`, adicionamos a aplicação `accounts` colocando `accounts.apps.AccountsConfig`;
- No arquivo `urls.py` do projeto, adicionamos a rota `accounts/`, no `urlpatterns` colocando `path('accounts/', include('accounts.urls'))`;
- Criamos o arquivo `urls.py` da aplicação `accounts`, e adicionamos o seguinte:

```python
# Arquivo: accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

```

Com essas urls configuradas, vamos então acessar `accounts/views.py` e adicionar o seguinte:

```python
from django.shortcuts import render
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

```

Agora que temos as views criadas, temos que criar a pasta `templates`, nela criar a pasta `accounts` e dentro dela criar o arquivo `login.html`, `logout.html`, `register.html` e `dashboard.html`.

Observe que importamos o `messages` do Django para adicionar mensagens de feedback ao usuário.

Com todos esses arquivos criados, agora temos apenas que colocar o conteúdo de cada arquivo, que será o seguinte:

#### Login
Responsável por mostrar o formulário de login e fazer o login do usuário.

```html
<!-- Arquivo: accounts/login.html -->

{% extends 'base.html' %}

{% block 'conteudo' %}
<h1>Login</h1>
{% endblock %}

```

#### Logout
Responsável por deslogar o usuário.

```html
<!-- Arquivo: accounts/logout.html -->

{% extends 'base.html' %}

{% block 'conteudo' %}
<h1>Logout</h1>
{% endblock %}

```

#### Register
Responsável pelo cadastro de novos usuários.

```html
<!-- Arquivo: accounts/register.html -->

{% extends 'base.html' %}

{% block 'conteudo' %}
<h1>Register</h1>
{% endblock %}

```

#### Dashboard
Responsável por mostrar o painel do usuário.

```html
<!-- Arquivo: accounts/dashboard.html -->

{% extends 'base.html' %}

{% block 'conteudo' %}
<h1>Dashboard</h1>
{% endblock %}

```

### Criando a tela de cadastro

No arquivo `accounts/register.html`, adicionamos o seguinte:

```html
<!-- Arquivo: accounts/register.html -->

{% extends 'base.html' %}

{% block 'conteudo' %}
<h1 class="mt-3 mb-3">Cadastro</h1>

<!-- Formulário de cadastro -->
<!-- O método que será utilizado é o POST e será enviado para a URL `accounts/register/` -->
<form method="POST" action="{% url 'register' %}">
    <!-- Incluímos os alertas que serão listados através do `messages.add_message()` -->
    {% include 'partials/_messages.html' %}
    <!-- csrf_token é um token de segurança que é gerado automaticamente pelo Django -->
    {% csrf_token %}
    <div class="form-row">
        <div class="form-group col-md-6">
            <label for="name">Nome</label>
            <input type="text" class="form-control" id="name" name="name" placeholder="Digite seu nome">
        </div>
        <div class="form-group col-md-6">
            <label for="lastname">Sobrenome</label>
            <input type="text" class="form-control" id="lastname" name="lastname" placeholder="Digite seu sobrenome">
        </div>
    </div>
    <div class="form-group">
        <label for="username">Usuário</label>
        <input type="text" class="form-control" id="username" name="username" placeholder="Digite seu usuário">
    </div>

    <div class="form-group">
        <label for="email">E-mail</label>
        <input type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp"
               placeholder="Digite seu e-mail">
        <small id="emailHelp" class="form-text text-muted">Nunca compartilharemos o seu e-mail com mais ninguém.</small>
    </div>

    <div class="form-row">
        <div class="form-group col-md-6">
            <label for="password">Senha</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Digite sua senha">
        </div>

        <div class="form-group col-md-6">
            <label for="password_confirmation">Confirmar senha</label>
            <input type="password" class="form-control" id="password_confirmation" name="password_confirmation"
                   placeholder="Confirme sua senha">
        </div>
    </div>


    <button type="submit" class="btn btn-primary">Cadastrar</button>
</form>

{% endblock %}

```

Adicionamos o formulário que será utilizado para o cadastro de usuários, para que seja recebido os dados, é necessário passar o atributo `name` para cada campo.

Apenas uma modificação que foi feita no arquivo `base.html`, foi adicionado um `if` para mostrar o campo de pesquisa somente se na rota não tiver o caminho `accounts`, da seguinte forma:

```html
<!-- Arquivo: base.html -->

<!-- [...] -->
<div class="col-lg-12">

    {% if 'accounts' not in request.path %}
    <form method="get" action="{% url 'busca' %}">
        <div class="form-group row">
            <div class="col-12">
                <input class="form-control"
                       type="search" value="{{ request.GET.termo }}"
                       id="search-input"
                       placeholder="Digite sua pesquisa"
                       name="termo">
            </div>
        </div>
    </form>

    {% include 'partials/_messages.html' %}
    {% endif %}

    {% block 'conteudo' %}{% endblock %}
</div>
<!-- [...] -->
```

Foi apenas envolvido o campo de pesquisa com o critério `if 'accounts' not in request.path` para que o mesmo não apareça na tela de cadastro, login e dashboard.

## Criando função de criar usuário

Para criação de usuário, vamos ao arquivo `accounts/views.py` e na função `register` adicionamos o seguinte:

```python
# Arquivo: accounts/views.py

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
```

- Primeiro então, pegamos todos os dados recebidos na requisição através do método `POST` e armazenamos em variáveis.
- Verificamos se todos os campos foram preenchidos, caso não sejam, retornamos uma mensagem de erro.
- Verificamos se o nome e sobrenome possuem mais de 2 caracteres, caso não sejam, retornamos uma mensagem de erro.
- Verificamos se o nome de usuário possui pelo menos 6 caracteres, caso não seja, retornamos uma mensagem de erro.
- Verificamos se o nome de usuário já existe, caso exista, retornamos uma mensagem de erro.
- Verificamos se o email já existe, caso exista, retornamos uma mensagem de erro.
- Verificamos se o email é válido, caso não seja, retornamos uma mensagem de erro.
- Verificamos se a senha possui pelo menos 8 caracteres, caso não seja, retornamos uma mensagem de erro.
- AVerificamos se as senhas são iguais, caso não sejam, retornamos uma mensagem de erro.
- Caso passe por todas as validações, criamos o usuário, salvamos no banco de dados e retornamos uma mensagem de sucesso.
- Redirecionamos o usuário para a tela de login.

> **Nota:**
> Foi feito uma pequena modificação no `register.html` para que quando ocorra algum erro, os campos voltem populados com os dados já preenchidos, utilizando `value="{{request.POST.NAME_DO_CAMPO}}"` para isso.
> 
> Além disso, nos campos de senha e usuário, foi adicionado um `aria-describedby="ID_CAMPO_AJUDA"` para que o usuário saiba como preencher o campo.