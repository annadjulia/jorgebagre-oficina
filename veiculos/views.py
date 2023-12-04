from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Veiculo, Cliente

# Create your views here.
def veiculos(request):
    veiculos = Veiculo.objects.all()
    msg = request.GET.get('msg')
    if msg == None:
        msg = ''
    msgType = request.GET.get('msgType')
    if msgType == None:
        msgType = ''
    return render(request, 'veiculos.html', {'veiculos': veiculos, 'msg': msg, 'msgType': msgType})

def new_veiculo(request):
    clientes = Cliente.objects.all()
    if request.method == 'GET':
        return render(request, 'new_veiculo.html', {'clientes': clientes})
    elif request.method == 'POST':
        placa = request.POST.get('placa')
        modelo = request.POST.get('modelo')
        descricao = request.POST.get('descricao')
        cliente_id = request.POST.get('cliente_id')
        print(placa, modelo, descricao, cliente_id)
        
        veiculo = Veiculo.objects.filter(placa=placa)
        if veiculo.exists():
            print('Veiculo já cadastrado.')
            return render(request, 'new_veiculo.html', {'msg': 'Veiculo já cadastrado.', 'msgType': 'error' ,'clientes': clientes})
        elif len(placa) != 7:
            print('Placa inválida.')
            return render(request, 'new_veiculo.html', {'msg': 'Placa inválida.', 'msgType': 'error' ,'clientes': clientes})
        elif len(modelo) < 3:
            print('Modelo inválido.')
            return render(request, 'new_veiculo.html', {'msg': 'Modelo inválido.', 'msgType': 'error' ,'clientes': clientes})
        elif cliente_id == '0':
            print('Selecione um cliente.')
            return render(request, 'new_veiculo.html', {'msg': 'Selecione um cliente.', 'msgType': 'error' ,'clientes': clientes})

        veiculo = Veiculo(placa=placa, modelo=modelo, descricao=descricao, cliente_id=cliente_id)
        veiculo.save()

        return HttpResponseRedirect('/veiculos', {'msg': 'Veiculo cadastrado com sucesso.', 'msgType': 'success'})

def view_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    cliente = Cliente.objects.get(id=veiculo.cliente_id)
    return render(request, 'view_veiculo.html', {'veiculo': veiculo, 'cliente': cliente})

def edit_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    clientes = Cliente.objects.all()
    if request.method == 'GET':
        return render(request, 'edit_veiculo.html', {'veiculo': veiculo, 'clientes': clientes})
    elif request.method == 'POST':
        placa = request.POST.get('placa')
        modelo = request.POST.get('modelo')
        descricao = request.POST.get('descricao')
        cliente_id = request.POST.get('cliente_id')
        print(placa, modelo, descricao, cliente_id)
        
        veiculo = Veiculo.objects.filter(placa=placa)
        if veiculo.exists():
            print('Veiculo já cadastrado.')
            return render(request, 'edit_veiculo.html', {'msg': 'Veiculo já cadastrado.', 'msgType': 'error' ,'clientes': clientes, 'veiculo': veiculo})
        elif len(placa) != 7:
            print('Placa inválida.')
            return render(request, 'edit_veiculo.html', {'msg': 'Placa inválida.', 'msgType': 'error' ,'clientes': clientes, 'veiculo': veiculo})
        elif len(modelo) < 3:
            print('Modelo inválido.')
            return render(request, 'edit_veiculo.html', {'msg': 'Modelo inválido.', 'msgType': 'error' ,'clientes': clientes, 'veiculo': veiculo})
        elif cliente_id == '0':
            print('Selecione um cliente.')
            return render(request, 'edit_veiculo.html', {'msg': 'Selecione um cliente.', 'msgType': 'error' ,'clientes': clientes, 'veiculo': veiculo})

        veiculo.placa = placa
        veiculo.modelo = modelo
        veiculo.descricao = descricao
        veiculo.cliente_id = cliente_id
        veiculo.save()

        return HttpResponseRedirect('/veiculos', {'msg': 'Veiculo editado com sucesso.', 'msgType': 'success'})
    
def delete_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    veiculo.delete()
    return HttpResponseRedirect('/veiculos', {'msg': 'Veiculo deletado com sucesso.', 'msgType': 'success'})
