from django.urls import path
from CadastroCliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.listar_clientes, name='clientes'),
    path('profissao/', views.profissao, name='profissao'),
    path('cliente', views.detalhar_cliente, name='detalhar')

]
