from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cliente
from veiculos.models import Veiculo

# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    msg = request.GET.get('msg')
    if msg == None:
        msg = ''
        msgType = ''
    return render(request, 'clientes.html', {'clientes': clientes, 'msg': msg, 'msgType': msgType})

def new_cliente(request):
    if request.method == 'GET':
        return render(request, 'new_cliente.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        print(nome, email, cpf, telefone)

        busca_cliente = Cliente.objects.filter(cpf=cpf)
        if busca_cliente.exists():
            print('Cliente já cadastrado.')
            return render(request, 'new_cliente.html', {'msg': 'Cliente já cadastrado.', 'msgType': 'error'})
        elif len(cpf) != 14:
            print('CPF inválido.'+cpf)
            return render(request, 'new_cliente.html', {'msg': 'CPF inválido.', 'msgType': 'error'})
        elif len(telefone) != 15:
            print('Telefone inválido.')
            return render(request, 'new_cliente.html', {'msg': 'Telefone inválido.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_cliente.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        elif len(email) < 3:
            print('Email inválido.')
            return render(request, 'new_cliente.html', {'msg': 'Email inválido.', 'msgType': 'error'})

        cliente = Cliente(nome=nome, email=email, cpf=cpf, telefone=telefone)
        cliente.save()

        return HttpResponseRedirect('/clientes', {'msg': 'Cliente editado com sucesso.', 'msgType': 'success'})

def view_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    veiculos = Veiculo.objects.filter(cliente_id=id)
    return render(request, 'view_cliente.html', {'cliente': cliente, 'veiculos': veiculos})

def edit_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit_cliente.html', {'cliente': cliente})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        print(nome, email, cpf, telefone)

        busca_cliente = Cliente.objects.filter(cpf=cpf).exclude(id=id)
        if busca_cliente.exists():
            print('Cliente já cadastrado.')
            return render(request, 'edit_cliente.html', {'msg': 'Cliente já cadastrado.', 'msgType': 'error', 'cliente': cliente})
        elif len(cpf) != 14:
            print('CPF inválido.'+cpf)
            return render(request, 'edit_cliente.html', {'msg': 'CPF inválido.', 'msgType': 'error', 'cliente': cliente})
        elif len(telefone) != 15:
            print('Telefone inválido.')
            return render(request, 'edit_cliente.html', {'msg': 'Telefone inválido.', 'msgType': 'error', 'cliente': cliente})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'edit_cliente.html', {'msg': 'Nome inválido.', 'msgType': 'error', 'cliente': cliente})
        elif len(email) < 3:
            print('Email inválido.')
            return render(request, 'edit_cliente.html', {'msg': 'Email inválido.', 'msgType': 'error', 'cliente': cliente})

        cliente = Cliente.objects.get(id=id)
        cliente.nome = nome
        cliente.email = email
        cliente.cpf = cpf
        cliente.telefone = telefone
        cliente.save()

        return HttpResponseRedirect('/clientes', {'msg': 'Cliente editado com sucesso.', 'msgType': 'success', 'cliente': cliente})
    
def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return HttpResponseRedirect('/clientes', {'msg': 'Cliente deletado com sucesso.', 'msgType': 'success', 'cliente': cliente})    
