from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = 'Rodrigo Reis'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome': meu_nome,
        'frutas': lista_frutas
    }

    return render(request, 'index.html', context)