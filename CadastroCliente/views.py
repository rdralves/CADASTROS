from django.shortcuts import render
from CadastroCliente.models import Cliente, Profissao, Telefone

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
    lista_profissao = Profissao.objects.all()
    lista_clientes = Cliente.objects.all()
    context = {
        "clientes": lista_clientes,
        'profissoes': lista_profissao
    }
    return render(request, 'listar_clientes.html', context)


def profissao(request):
    lista_profissao = Profissao.objects.all()
    context = {
        'profissoes': lista_profissao
    }

    return render(request, 'listar_profissao.html', context)


def detalhar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    telefones = Telefone.objects.filter(cliente_id = id)[:3]
    context = {
        "cliente": cliente,
        "telefones": telefones,
    }
    return render(request, 'cliente_detalhe.html', context)