from django.shortcuts import render
from CadastroCliente.models import Cliente

# Create your views here.
def index(request):
    meu_nome = 'Rodrigo Reis'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome': meu_nome,
        'frutas': lista_frutas
    }

    return render(request, 'index.html', context)


def listar_clientes(request):
    return render(request, 'listar_clientes.html')
