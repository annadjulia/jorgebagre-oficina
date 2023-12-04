from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Mecanico
from equipes.models import Equipe

# Create your views here.
def mecanicos(request):
    return render(request, 'mecanicos.html')

def new_mecanico(request):
    if request.method == 'GET':
        return render(request, 'new_mecanico.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        especialidade = request.POST.get('especialidade')
        equipe_id = request.POST.get('equipe_id')
        print(nome, email, cpf, telefone, especialidade, equipe_id)

        busca_mecanico = Mecanico.objects.filter(cpf=cpf)
        if busca_mecanico.exists():
            print('Mecanico já cadastrado.')
            return render(request, 'new_mecanico.html', {'msg': 'Mecanico já cadastrado.', 'msgType': 'error'})
        elif len(cpf) != 14:
            print('CPF inválido.'+cpf)
            return render(request, 'new_mecanico.html', {'msg': 'CPF inválido.', 'msgType': 'error'})
        elif len(telefone) != 15:
            print('Telefone inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Telefone inválido.', 'msgType': 'error'})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Nome inválido.', 'msgType': 'error'})
        elif len(email) < 3:
            print('Email inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Email inválido.', 'msgType': 'error'})
        
        mecanico = Mecanico(nome=nome, email=email, cpf=cpf, telefone=telefone, especialidade=especialidade, equipe_id=equipe_id)
        mecanico.save()

        return HttpResponseRedirect('/mecanicos', {'msg': 'Mecanico cadastrado com sucesso.', 'msgType': 'success'})
        

def view_mecanico(request, id):
    mecanico = Mecanico.objects.get(id=id)
    equipe = Equipe.objects.get(id=mecanico.equipe_id)
    return render(request, 'view_mecanico.html', {'mecanico': mecanico, 'equipe': equipe})

def edit_mecanico(request, id):
    mecanico = Mecanico.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit_mecanico.html', {'mecanico': mecanico})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        especialidade = request.POST.get('especialidade')
        equipe_id = request.POST.get('equipe_id')
        print(nome, email, cpf, telefone, especialidade, equipe_id)

        busca_mecanico = Mecanico.objects.filter(cpf=cpf)
        if busca_mecanico.exists():
            print('Mecanico já cadastrado.')
            return render(request, 'new_mecanico.html', {'msg': 'Mecanico já cadastrado.', 'msgType': 'error', 'mecanico': mecanico})
        elif len(cpf) != 14:
            print('CPF inválido.'+cpf)
            return render(request, 'new_mecanico.html', {'msg': 'CPF inválido.', 'msgType': 'error', 'mecanico': mecanico})
        elif len(telefone) != 15:
            print('Telefone inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Telefone inválido.', 'msgType': 'error', 'mecanico': mecanico})
        elif len(nome) < 3:
            print('Nome inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Nome inválido.', 'msgType': 'error', 'mecanico': mecanico})
        elif len(email) < 3:
            print('Email inválido.')
            return render(request, 'new_mecanico.html', {'msg': 'Email inválido.', 'msgType': 'error', 'mecanico': mecanico})
        
        mecanico = Mecanico(nome=nome, email=email, cpf=cpf, telefone=telefone, especialidade=especialidade, equipe_id=equipe_id)
        mecanico.save()

        return HttpResponseRedirect('/mecanicos', {'msg': 'Mecanico editado com sucesso.', 'msgType': 'success', 'mecanico': mecanico})

def delete_mecanico(request, id):
    mecanico = Mecanico.objects.get(id=id)
    mecanico.delete()
    return HttpResponseRedirect('/mecanicos', {'msg': 'Mecanico deletado com sucesso.', 'msgType': 'success', 'mecanico': mecanico})