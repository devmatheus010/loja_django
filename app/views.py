from django.shortcuts import render, get_object_or_404
from .models import Produto

def lista_tecnologia(request):
    produtos = Produto.objects.filter(categoria='tecnologia')
    return render(request, 'app/lista_tecnologia.html', {'produtos': produtos})

def lista_vestuario(request):
    produtos = Produto.objects.filter(categoria='vestuario')
    return render(request, 'app/lista_vestuario.html', {'produtos': produtos})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'app/detalhes.html', {'produto': produto})
