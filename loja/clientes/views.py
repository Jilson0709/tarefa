from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

# Exibe a lista de clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

# Exibe o formulário para cadastro de cliente
def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)
        return redirect('listar_clientes')
    return render(request, 'clientes/cadastrar.html')

# Exibe o formulário para editar um cliente existente
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nome = request.POST['nome']
        cliente.email = request.POST['email']
        cliente.telefone = request.POST['telefone']
        cliente.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/editar.html', {'cliente': cliente})

# Exclui um cliente
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/excluir.html', {'cliente': cliente})


# Create your views here.
