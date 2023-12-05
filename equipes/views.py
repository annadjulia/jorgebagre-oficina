from django.shortcuts import render
from .models import Equipe
from mecanicos.models import Mecanico

from django.http import HttpResponseRedirect

# Create your views here.
def equipes(request):
    equipes = Equipe.objects.all()
    return render(request, 'equipes.html', {'equipes': equipes})

def new_equipe(request):
    if request.method == 'GET':
        return render(request, 'new_equipe.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        print(nome)

        busca_equipe = Equipe.objects.filter(nome=nome)
        if busca_equipe.exists():
            print('Equipe já cadastrada.')
            return render(request, 'new_equipe.html', {'msg': 'Equipe já cadastrada.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_equipe.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        
        equipe = Equipe(nome=nome)
        equipe.save()

        return HttpResponseRedirect('/equipes', {'msg': 'Equipe cadastrada com sucesso.', 'msgType': 'success', 'equipes': equipes})
    
def view_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    mecanicos = Mecanico.objects.filter(equipe_id=id)
    return render(request, 'view_equipe.html', {'equipe': equipe, 'mecanicos': mecanicos})

def edit_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit_equipe.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        print(nome)

        busca_equipe = Equipe.objects.filter(nome=nome)
        if busca_equipe.exists():
            print('Equipe já cadastrada.')
            return render(request, 'edit_equipe.html', {'msg': 'Equipe já cadastrada.', 'msgType': 'error', 'equipe': equipe})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'edit_equipe.html', {'msg': 'Nome inválido.', 'msgType': 'error', 'equipe': equipe})
        
        equipe = Equipe(nome=nome)
        equipe.save()

        return HttpResponseRedirect('/equipes', {'msg': 'Equipe cadastrada com sucesso.', 'msgType': 'success'})

def delete_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    equipe.delete()
    return HttpResponseRedirect('/equipes', {'msg': 'Equipe deletada com sucesso.', 'msgType': 'success', 'equipes': equipes})