from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Peca

# Create your views here.
def pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas.html', {'pecas': pecas})

def new_peca(request):
    if request.method == 'GET':
        return render(request, 'new_peca.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        busca_peca = Peca.objects.filter(nome=nome)
        if busca_peca.exists():
            print('Peça já cadastrada.')
            return render(request, 'new_peca.html', {'msg': 'Peça já cadastrada.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_peca.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        elif len(preco) < 1:
            print('Preço inválido.')
            return render(request, 'new_peca.html', {'msg': 'Preço inválido.', 'msgType': 'error'})
        
        peca = Peca(nome=nome, preco=preco)
        peca.save()

        return HttpResponseRedirect('/pecas', {'msg': 'Peça cadastrada com sucesso.', 'msgType': 'success'})

def view_peca(request, id):
    peca = Peca.objects.get(id=id)
    return render(request, 'view_peca.html', {'peca': peca})

def edit_peca(request, id):
    peca = Peca.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit_peca.html', {'peca': peca})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        busca_peca = Peca.objects.filter(nome=nome)
        if busca_peca.exists():
            print('Peça já cadastrada.')
            return render(request, 'edit_peca.html', {'msg': 'Peça já cadastrada.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'edit_peca.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        elif len(preco) < 1:
            print('Preço inválido.')
            return render(request, 'edit_peca.html', {'msg': 'Preço inválido.', 'msgType': 'error'})
        
        peca.nome = nome
        peca.preco = preco
        peca.save()

        return HttpResponseRedirect('/pecas', {'msg': 'Peça editada com sucesso.', 'msgType': 'success'})

def delete_peca(request, id):
    peca = Peca.objects.get(id=id)
    peca.delete()
    return HttpResponseRedirect('/pecas', {'msg': 'Peça deletada com sucesso.', 'msgType': 'success'})  