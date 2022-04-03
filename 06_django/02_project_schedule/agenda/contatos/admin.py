from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar',)
    list_filter = ('categoria',)
    search_fields = ('nome', 'email', 'telefone')
    ordering = ('id',)
    list_per_page = 5


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
