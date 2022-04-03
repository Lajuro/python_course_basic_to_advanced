from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


