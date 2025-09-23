from django.contrib import admin
from app.models import Produto

@admin.register(Produto)
class Produto(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'imagem', 'categoria')
    list_filter = ('categoria', )

