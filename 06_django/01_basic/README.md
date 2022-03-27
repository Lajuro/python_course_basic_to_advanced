# Criando um projeto Django [Hello World]

Para criação de um projeto `Django`, é necessário ter o `Python 3.6` ou superior instalado.

Para instalar o Django via pip, rode o comando abaixo:

```shell
  pip install django
```

O comando para criar um projeto Django é o seguinte:

```shell
  django-admin startproject <nome_do_projeto> <caminho_do_projeto>
```

---

Todos os aplicativos que forem criados podem ser criados dentro de um projeto Django.

- **INSTALLED_APPS** é uma lista de aplicativos que estão instalados no projeto Django.
- **MIDDLEWARE** é uma lista de aplicativos que serão executados antes de qualquer requisição.
- **TEMPLATES** é uma lista de templates que serão utilizados para renderizar o conteúdo.
  - **BACKEND** é o tipo de template que será utilizado.
  - **DIRS** é uma lista de diretórios que serão utilizados para buscar os templates.
  - **APP_DIRS** é um booleano que indica se o Django irá buscar os templates dentro dos diretórios dos aplicativos.
  - **OPTIONS** é um dicionário que pode ser utilizado para configurar o Django.
  - **LOADERS** é uma lista de loaders que serão utilizados para buscar os templates.
- **STATICFILES_DIRS** é uma lista de diretórios que serão utilizados para armazenar arquivos estáticos.
- **STATIC_URL** é a URL para o diretório de arquivos estáticos.
- **STATIC_ROOT** é o diretório onde os arquivos estáticos serão armazenados.
- **MEDIA_URL** é a URL para o diretório de arquivos de mídia.
- **MEDIA_ROOT** é o diretório onde os arquivos de mídia serão armazenados.
- **SECRET_KEY** é uma chave secreta para criptografar dados.
- **ALLOWED_HOSTS** é uma lista de hosts que podem acessar o projeto Django.
- **DEBUG** é um valor booleano que indica se o projeto está em modo de depuração.
- **LANGUAGE_CODE** é o código de idioma padrão para o projeto Django.
- **TIME_ZONE** é o fuso horário padrão para o projeto Django.
- **USE_I18N** é um valor booleano que indica se o projeto Django deve utilizar internacionalização.
- **USE_L10N** é um valor booleano que indica se o projeto Django deve utilizar localização.
- **USE_TZ** é um valor booleano que indica se o projeto Django deve utilizar fuso horário.
- **STATICFILES_FINDERS** é uma lista de aplicativos que serão utilizados para encontrar arquivos estáticos.
- O arquivo `asgi.py` é um arquivo de configuração do projeto Django.
- O arquivo `wsgi.py` é um arquivo que é responsável por iniciar o servidor web.
- O arquivo `manage.py` é o arquivo principal do projeto Django. Ele é responsável por executar os comandos do Django.
- O arquivo `settings.py` é o arquivo de configuração do projeto Django.
- O arquivo `urls.py` é o arquivo de configuração das URLs do projeto Django.

## Iniciando o servidor

Para iniciar o servidor, basta executar o comando:

```shell
  python manage.py runserver
```

Deve estar na mesma pasta do projeto Django.

Caso desejar rodar numa porta diferente, basta executar o comando:

```shell
  python manage.py runserver <porta>
```

## Começar uma nova aplicação

Para criar uma nova aplicação, basta executar o comando:

```shell
    python manage.py startapp <nome_da_aplicação>
```

Para registrar a aplicação no projeto Django, deve adiciona-la na lista `INSTALLED_APPS` do arquivo `settings.py`

### Informações sobre o passo a passo para criar uma aplicação

1. Rode o comando `python manage.py startapp <nome_da_aplicação>` para criar a aplicação.
2. Adicione no `INSTALLED_APPS` do arquivo `settings.py` a classe da aplicação conforme está no arquivo `apps`.
3. No arquivo `urls.py` adicione o include utilizando o comando `path('<caminho_para_a_aplicação>', include('<nome_da_aplicação>.urls'))`.
4. Na aplicação criada, crie um arquivo `urls.py` e adicione as URLs da aplicação em uma lista de URLs utilizando o comando `path('<caminho_para_a_aplicação>', views.<nome_do_metodo>)`.
5. No arquivo `views.py` crie um método com o nome informado na URL do arquivo `urls.py`.
6. Caso esteja renderizando um template, crie um arquivo `templates/<nome_da_aplicação>/<nome_do_template>.html`.
7. No arquivo `templates/<nome_da_aplicação>/<nome_do_template>.html` crie um bloco de HTML com o nome informado na URL do arquivo `urls.py`.
8. Rode o comando `python manage.py runserver` para iniciar o servidor.
9. Acesse a URL informada na URL do arquivo `urls.py`.

Com esses poucos passos já terá a aplicação criada e funcionando.

### Informação de como definir uma pasta de templates

1. No arquivo `settings.py`, dentro de `TEMPLATES`, defina o parâmetro `DIRS` com o caminho onde ficará a pasta de templates.
   - **Exemplo:** `TEMPLATES = [{'DIRS': [os.path.join(BASE_DIR, 'templates')]}]`
   - **Observação:** O caminho deve ser relativo ao diretório do projeto Django.

### Como criar uma página home para a rota principal

Existem duas formas de criar uma página home para a rota principal:

1. Utilizar o próprio diretório do projeto Django.
   1. No arquivo `urls.py`, adicione a URL `path('', views.<nome_do_metodo>)`, não esquecendo de importar o método `views`.
   2. No arquivo `views.py`, crie um método com o nome `home` e retorne o template `home.html`.
   3. Rode o comando `python manage.py runserver` para iniciar o servidor.
   4. Acesse a URL `http://localhost:<porta>/`.
2. Criar uma aplicação para a home.
   1. Crie uma aplicação chamada `home` rodando o comando `python manage.py startapp home`.
   2. Adicione no `INSTALLED_APPS` do arquivo `settings.py` a classe da aplicação `home` que será `home.apps.HomeConfig`.
   3. No arquivo `urls.py`, adicione a URL `path('', include('home.urls'))`.
   4. No arquivo `home/urls.py`, adicione a URL `path('', views.<nome_do_metodo>)`.
   5. No arquivo `home/views.py`, crie um método com o nome `home` e retorne o template `home.html`.
   6. Rode o comando `python manage.py runserver` para iniciar o servidor.
   7. Acesse a URL informada na URL do arquivo `home/urls.py`.

### Como configurar arquivos estáticos (CSS, JS, imagens)

- Para configurar o seu projeto Django para utilizar arquivos estáticos (CSS, JS, imagens), deve-se adicionar o parâmetro `STATICFILES_DIRS` no arquivo `settings.py` e definir o caminho para o diretório onde os arquivos estáticos serão armazenados, por padrão, o caminho é `static`.
  - **Exemplo:** `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]` ou `STATICFILES_DIRS = [BASE_DIR / 'templates/static]`

- Dentro do arquivo HTML, utilize `{% load static %}` para importar os arquivos estáticos. Para que o arquivo seja carregado, deve-se utilizar o comando `{% static '<nome_do_arquivo>' %}`.
  - **Exemplo:** `{% static 'css/style.css' %}`

- Mas também, sem nenhuma configuração, o Django irá carregar os arquivos estáticos automaticamente, para isso adicione uma pasta chamada `static` no diretório raiz do projeto e então coloque os arquivos estáticos dentro dela.