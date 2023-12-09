from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Ordem
from clientes.models import Cliente
from veiculos.models import Veiculo
from equipes.models import Equipe
from pecas.models import Peca
from servicos.models import Servico
import datetime

# Create your views here.
def ordens(request):
    ordens = Ordem.objects.all()
    return render(request, 'ordens.html', {'ordens': ordens})

def new_ordem(request):
    clientes = Cliente.objects.all()
    veiculos = Veiculo.objects.all()
    equipes = Equipe.objects.all()
    #pecas = Peca.objects.all()
    #servicos = Servico.objects.all()
    if request.method == 'GET':
        return render(request, 'new_ordem.html', {'clientes': clientes, 'veiculos': veiculos, 'equipes': equipes, 'pecas': pecas, 'servicos': servicos})
    elif request.method == 'POST':
        dataEmissao = datetime.date.today()
        dataEntrega = request.POST.get('dataEntrega')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        status = request.POST.get('status')
        veiculo_id = request.POST.get('veiculo_id')
        equipe_id = request.POST.get('equipe_id')
        print(dataEmissao, dataEntrega, descricao, valor, status, veiculo_id, equipe_id)

        busca_ordem = Ordem.objects.filter(descricao=descricao)
        if busca_ordem.exists():
            print('Ordem já cadastrada.')
            return render(request, 'new_ordem.html', {'msg': 'Ordem já cadastrada.', 'msgType': 'error'})
        elif len(descricao) < 3:
            print('Descrição inválida.')
            return render(request, 'new_ordem.html', {'msg': 'Descrição inválida.', 'msgType': 'error'})
        elif len(valor) < 1:
            print('Valor inválido.')
            return render(request, 'new_ordem.html', {'msg': 'Valor inválido.', 'msgType': 'error'})
        
        ordem = Ordem(dataEmissao=dataEmissao, dataEntrega=dataEntrega, descricao=descricao, valor=valor, status=status, veiculo_id=veiculo_id, equipe_id=equipe_id)
        ordem.save()

        return HttpResponseRedirect('/ordens', {'msg': 'Ordem cadastrada com sucesso.', 'msgType': 'success'})

def view_ordem(request, id):
    return render(request, 'view_ordem.html')

def edit_ordem(request, id):
    return render(request, 'edit_ordem.html')

def delete_ordem(request, id):
    return render(request, 'delete_ordem.html')