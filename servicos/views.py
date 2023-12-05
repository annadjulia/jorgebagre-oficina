from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Servico

# Create your views here.
def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

def new_servico(request):
    if request.method == 'GET':
        return render(request, 'new_servico.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        busca_servico = Servico.objects.filter(nome=nome)
        if busca_servico.exists():
            print('Serviço já cadastrado.')
            return render(request, 'new_servico.html', {'msg': 'Serviço já cadastrado.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_servico.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        elif len(preco) < 1:
            print('Preço inválido.')
            return render(request, 'new_servico.html', {'msg': 'Preço inválido.', 'msgType': 'error'})
        
        servico = Servico(nome=nome, preco=preco)
        servico.save()

        return HttpResponseRedirect('/servicos', {'msg': 'Serviço cadastrado com sucesso.', 'msgType': 'success'})

def view_servico(request, id):
    servico = Servico.objects.get(id=id)
    return render(request, 'view_servico.html', {'servico': servico})

def edit_servico(request, id):
    servico = Servico.objects.get(id=id)
    return render(request, 'edit_servico.html', {'servico': servico})

def delete_servico(request, id):
    servico = Servico.objects.get(id=id)
    servico.delete()
    return HttpResponseRedirect('/servicos', {'msg': 'Serviço deletado com sucesso.', 'msgType': 'success'})