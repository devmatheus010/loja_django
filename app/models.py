from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
            ('tecnologia', 'Tecnologia'),
            ('vestuario', 'Vestuario')
    ]

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.nome
